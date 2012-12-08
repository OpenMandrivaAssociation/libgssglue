%define	major 1
%define libname	%mklibname gssglue %{major}
%define develname %mklibname gssglue -d

Summary:	A mechanism-switch gssapi library
Name:		libgssglue
Version:	0.4
Release:	1
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


%changelog
* Fri Jul 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-1mdv2011.0
+ Revision: 688427
- update to new version 0.3

* Thu Jun 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.2-1
+ Revision: 685573
- update to new version 0.2

* Fri Apr 29 2011 Funda Wang <fwang@mandriva.org> 0.1-9
+ Revision: 660620
- fix usage of multiarch

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-8mdv2011.0
+ Revision: 601046
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-7mdv2010.1
+ Revision: 520142
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1-6mdv2010.0
+ Revision: 425562
- rebuild

* Thu Dec 18 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1-5mdv2009.1
+ Revision: 315566
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2009.0
+ Revision: 222883
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.1-3mdv2008.1
+ Revision: 150688
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - spec cleanup

* Wed Sep 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-2mdv2008.0
+ Revision: 80167
- spec cleanup

  + Oden Eriksson <oeriksson@mandriva.com>
    - major and deps fixes

* Wed Sep 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-1mdv2008.0
+ Revision: 79930
- renaming to libgssglue
- renaming to libgssglue
- new version

* Mon Apr 23 2007 Andreas Hasenack <andreas@mandriva.com> 0.11-1mdv2008.0
+ Revision: 17623
- updated to version 0.11

