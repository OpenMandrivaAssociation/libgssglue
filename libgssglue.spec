%define	major 1
%define libname	%mklibname gssglue %{major}
%define develname %mklibname gssglue -d

Summary:	A mechanism-switch gssapi library
Name:		libgssglue
Version:	0.3
Release:	2
License:	BSD-like
Group:		System/Libraries
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:        http://www.citi.umich.edu/projects/nfsv4/linux/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	krb5-devel >= 1.3

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
Requires:	%{libname} >= %{version}-%{release}
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

%multiarch_includes %{buildroot}%{_includedir}/gssglue/gssapi/gssapi.h

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{multiarch_includedir}/gssglue/gssapi/gssapi.h
%{_includedir}/gssglue/gssapi/gssapi.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgssglue.pc
