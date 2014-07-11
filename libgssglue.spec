%bcond_without  uclibc
%define	major	1
%define libname	%mklibname gssglue %{major}
%define devname %mklibname gssglue -d

Summary:	A mechanism-switch gssapi library
Name:		libgssglue
Version:	0.4
Release:	12
License:	BSD-like
Group:		System/Libraries
Url:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:        http://www.citi.umich.edu/projects/nfsv4/linux/%{name}/%{name}-%{version}.tar.gz
Patch0:		libgssglue-aarch64.patch
BuildRequires:	krb5-devel >= 1.3
%if %{with uclibc}
BuildRequires:	uClibc-devel >= 0.9.33.2-15
%endif

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

%if %{with uclibc}
%package -n	uclibc-%{libname}
Summary:	A mechanism-switch gssapi library
Group:		System/Libraries

%description -n	uclibc-%{libname}
libgssapi provides a gssapi interface, but does not implement any
gssapi mechanisms itself; instead it calls other gssapi functions
(e.g., those provided by MIT Kerberos), depending on the requested
mechanism, to do the work.
%endif

%package -n	%{devname}
Summary:	Development library and header files for the libgssapi library
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
%if %{with uclibc}
Requires:	uclibc-%{libname} >= %{version}-%{release}
%endif
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

TOP_DIR="$PWD"
CONFIGURE_TOP=..
%if %{with uclibc}
mkdir -p uclibc
pushd uclibc
%uclibc_configure \
	--disable-static
%make
popd
%endif

mkdir -p system
pushd system
%configure2_5x \
	--disable-static
%make
popd


%install
%if %{with uclibc}
%makeinstall_std -C uclibc
%endif
install -d %{buildroot}%{_sysconfdir}
%makeinstall_std -C system

%multiarch_includes %{buildroot}%{_includedir}/gssglue/gssapi/gssapi.h

rm -f %{buildroot}%{uclibc_root}%{_libdir}/pkgconfig/libgssglue.pc

%files -n %{libname}
%{_libdir}/libgssglue.so.%{major}*

%if %{with uclibc}
%files -n uclibc-%{libname}
%{uclibc_root}/%{_libdir}/libgssglue.so.%{major}*
%endif

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{multiarch_includedir}/gssglue/gssapi/gssapi.h
%{_includedir}/gssglue/gssapi/gssapi.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgssglue.pc
%if %{with uclibc}
%{uclibc_root}%{_libdir}/*.so
%endif
