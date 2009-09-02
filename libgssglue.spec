%define	name    libgssglue
%define	version 0.1
%define	release %mkrel 6
%define	major   1
%define libname	%mklibname gssglue %{major}
%define develname	%mklibname gssglue -d

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A mechanism-switch gssapi library
License:	BSD-like
Group:		System/Libraries
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:        http://www.citi.umich.edu/projects/nfsv4/linux/%{name}/%{name}-%{version}.tar.gz
%if %mdkversion >= 1020
BuildRequires:	multiarch-utils >= 1.0.3
%endif
BuildRequires:	krb5-devel >= 1.3
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
libgssglue provides a gssapi interface, but does not implement any
gssapi mechanisms itself; instead it calls other gssapi functions
(e.g., those provided by MIT Kerberos), depending on the requested
mechanism, to do the work.

%package -n	%{libname}
Summary:	A mechanism-switch gssapi library
Group:		System/Libraries

%description -n	%{libname}
libgssapi provides a gssapi interface, but does not implement any
gssapi mechanisms itself; instead it calls other gssapi functions
(e.g., those provided by MIT Kerberos), depending on the requested
mechanism, to do the work.

%package -n	%{develname}
Summary:	Static library and header files for the libgssapi library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	gssglue-devel = %{version}-%{release}
Obsoletes:	%{mklibname gssapi 2 -d}

%description -n	%{develname}
libgssapi provides a gssapi interface, but does not implement any
gssapi mechanisms itself; instead it calls other gssapi functions
(e.g., those provided by MIT Kerberos), depending on the requested
mechanism, to do the work.

This package contains the static libgssapi library and its
header files.

%prep
%setup -q
# lib64 fix
perl -pi -e "s|/usr/lib|%{_libdir}|g" doc/gssapi_mech.conf

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}

%makeinstall_std

%if %mdkversion >= 1020
%multiarch_includes %{buildroot}%{_includedir}/gssglue/gssapi/gssapi.h
%endif

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%if %mdkversion >= 1020
%multiarch %{multiarch_includedir}/gssglue/gssapi/gssapi.h
%endif
%{_includedir}/gssglue/gssapi/gssapi.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/libgssglue.pc
