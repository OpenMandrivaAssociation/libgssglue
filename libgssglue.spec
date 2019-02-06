%define	major	1
%define libname	%mklibname gssglue %{major}
%define devname %mklibname gssglue -d

Summary:	A mechanism-switch gssapi library
Name:		libgssglue
Version:	0.4
Release:	19
License:	BSD-like
Group:		System/Libraries
Url:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:        http://www.citi.umich.edu/projects/nfsv4/linux/%{name}/%{name}-%{version}.tar.gz
Patch0:		libgssglue-aarch64.patch
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

%package -n	%{devname}
Summary:	Development library and header files for the libgssapi library
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	gssglue-devel = %{version}-%{release}
Obsoletes:	%{mklibname gssapi 2 -d}

%description -n	%{devname}
This package contains the development libgssapi library and its
header files.

%prep
%setup -q
# lib64 fix
sed -i -e "s|/usr/lib|%{_libdir}|g" doc/gssapi_mech.conf
%patch0 -p1

%build
%ifarch %arm
export ac_cv_func_malloc_0_nonnull=yes
export ac_cv_func_realloc_0_nonnull=yes
%endif

%configure \
	--disable-static

%make


%install
install -d %{buildroot}%{_sysconfdir}
%makeinstall_std

rm -f %{buildroot}%{uclibc_root}%{_libdir}/pkgconfig/libgssglue.pc

%files -n %{libname}
%{_libdir}/libgssglue.so.%{major}*

%files -n %{devname}
%doc AUTHORS INSTALL NEWS README
%{_includedir}/gssglue/gssapi/gssapi.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgssglue.pc
