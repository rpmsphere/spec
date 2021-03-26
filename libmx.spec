Name:          libmx
Version:       1.4.7
Release:       21
Summary:       A clutter widget toolkit

Group:         System Environment/Libraries
License:       LGPLv2
URL:           http://www.clutter-project.org
Source0:       https://github.com/downloads/clutter-project/mx/mx-%{version}.tar.xz
Patch0:        0001-Replace-GL-data-types-with-equivalent-glib-types.patch

BuildRequires: clutter-devel
BuildRequires: dbus-glib-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: gtk2-devel
BuildRequires: pkgconfig
BuildRequires: startup-notification-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gtk-doc

%description
Mx is a clutter widget toolkit that provides a set of standard user interface 
elements, including buttons, progress bars, tooltips, scroll bars and others. 
It also implements some standard layout managers. One other interesting feature 
is the possibility of setting style properties from a css-like file. It is 
currently used by Moblin to provide the user experience.

%package devel
Summary: Development package for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: clutter-devel, gdk-pixbuf2-devel
Requires: pkgconfig

%description devel
Header files and libraries used for development with MX, a clutter widget 
toolkit, currently used primarily by Moblin.

%package docs
Summary: Documentation files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description docs
This package contains developer documentation for MX, a clutter widget 
toolkit, currently used primarily by Moblin.

%prep
%setup -q -n mx-%{version}
%patch0 -p1 -b .header

%build
%configure --disable-static --enable-introspection --enable-gtk-doc
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang mx-1.0

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f mx-1.0.lang
%doc COPYING.LIB README NEWS
%{_bindir}/mx-create-image-cache
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/Mx*.typelib
%{_datadir}/mx

%files devel
%{_includedir}/mx-1.0
%{_libdir}/pkgconfig/mx*.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/Mx*.gir

%files docs
%{_datadir}/gtk-doc/html/mx
%{_datadir}/gtk-doc/html/mx-gtk

%changelog
* Tue Dec 11 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.7
- Rebuild for Fedora

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.4.7-14
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 1.4.7-12
- Rebuilt for cogl soname bump

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 1.4.7-11
- Rebuild for libevdev soname bump

* Wed Feb 05 2014 Kalev Lember <kalevlember@gmail.com> - 1.4.7-10
- Rebuilt for cogl soname bump

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 1.4.7-9
- Rebuilt for cogl 1.15.4 soname bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Matthias Clasen <mclasen@redhat.com> - 1.4.7-7
- Ship NEWS instead of ChangeLog (much smaller)

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 1.4.7-6
- Rebuilt for cogl soname bump

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.7-5
- Rebuild for new cogl

* Wed Aug 29 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.4.7-4
- Use upstream patch to use glib data types instead of using GL definitions.

* Tue Aug 21 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.4.7-3
- Rebuild for new libcogl.
- Add patch to fix missing includes in src files.

* Sat Aug 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.7-2
- Rebuild for new cogl

* Tue Aug 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.7-1
- Release 1.4.7
- Update source location

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May  8 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.6-2
- Release 1.4.6

* Fri May 04 2012 Karsten Hopp <karsten@redhat.com> 1.4.5-1.1
- rebuild again on PPC, its still linked with old cogl

* Mon Apr  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.5-1
- Release 1.4.5

* Wed Mar 21 2012 Karsten Hopp <karsten@redhat.com> 1.4.3-3
- rebuild with new cogl (PPC)

* Sat Mar 10 2012 Matthias Clasen <mclasen@redhat.com> - 1.4.3-2
- Rebuild against new cogl

* Sat Mar 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.3-1
- Release 1.4.3

* Sun Feb 26 2012 Matthias Clasen <mclasen@redhat.com> - 1.4.1-5
- Rebuild against new cogl

* Thu Jan 19 2012 Matthias Clasen <mclasen@redhat.com> - 1.4.1-4
- Rebuild against new cogl

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 23 2011 Matthias Clasen <mclasen@redhat.com> - 1.4.1-2
- Rebuild against new clutter

* Mon Nov 21 2011 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.1-1
- Release 1.4.1

* Fri Oct 14 2011 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.0-1
- Release 1.4.0

* Thu Oct 06 2011 Bastien Nocera <bnocera@redhat.com> 1.3.2-1
- Update to 1.3.2

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> 1.3.1-2
- Rebuild

* Fri Sep 02 2011 Bastien Nocera <bnocera@redhat.com> 1.3.1-1
- Update to 1.3.1

* Fri Aug  5 2011 Tom Callaway <spot@fedoraproject.org> 1.3.0-2
- fix .pc file to require gdk-pixbuf-2.0

* Fri Aug  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.0-1
- 1.3.0
- Drop clutter-gestures and clutter-imcontext as they're not well supported

* Sun Jun  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0-1
- 1.2.0

* Fri May 13 2011 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.12-1
- New upstream 1.1.12

* Wed Apr 20 2011 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.11-1
- New upstream 1.1.11

* Sun Apr  3 2011 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.10-1
- New upstream 1.1.10

* Mon Mar 14 2011 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.9-1
- New upstream 1.1.9

* Thu Feb 17 2011 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.7-1
- New upstream 1.1.7

* Mon Feb 14 2011 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.6-1
- New upstream 1.1.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 28 2011 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.4-1
- New upstream 1.1.4

* Sat Jan 22 2011 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.3-1
- New upstream 1.1.3

* Mon Dec  6 2010 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-5
- Build against gtk3

* Fri Dec 03 2010 Dan Horák <dan[at]danny.cz> 1.1.0-4
- updated for clutter 1.4+

* Wed Sep 29 2010 jkeating - 1.1.0-3
- Rebuilt for gcc bug 634757

* Wed Sep 22 2010 Matthias Clasen <mclasen@redhat.com> 1.1.0-2
- Rebuild against newer gobject-introspection

* Sat Jul 31 2010 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-1
- New upstream 1.1.0 devel release

* Thu Jul 15 2010 Colin Walters <walters@verbum.org> - 1.0.3-2
- Rebuild with new gobject-introspection

* Sun Jul  4 2010 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.3-1
- New upstream 1.0.3 stable release

* Thu May 27 2010 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.2-1
- New upstream 1.0.2 stable release

* Sat May 22 2010 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.1-1
- New upstream 1.0.1 stable release, use official tar file

* Mon May 17 2010 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.0-1
- New upstream 1.0.0 stable release

* Sat May  1 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.8-1
- New upstream 0.99.8 release

* Mon Apr 26 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.7-1
- New upstream 0.99.7 release

* Sun Apr 18 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.5-1
- New upstream 0.99.5 release

* Wed Apr 14 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.4-2
- Upload new source file

* Wed Apr 14 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.4-1
- New upstream 0.99.4 release

* Thu Mar 25 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.0-2
- Add patch to fix build on gtk 2.2.20

* Thu Mar 25 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.0-1
- New upstream 0.9.0 release

* Sun Feb 28 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.3-1
- New upstream 0.7.3 release

* Sun Feb 21 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.1-1
- New upstream 0.6.1 release

* Fri Feb 12 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.0-2
- Upload source file

* Mon Feb  8 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.0-1
- New upstream 0.6.0 release

* Wed Feb  3 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.2-1
- New upstream 0.5.2 release

* Thu Jan 27 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.1-2
- Bump build

* Thu Jan 27 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.1-1
- New upstream 0.5.1 release

* Mon Jan 25 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.0-3
- Add dbus dep while we're at it!

* Mon Jan 25 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.0-2
- Add new dep

* Mon Jan 25 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.0-1
- New upstream 0.5.0 release

* Wed Jan 13 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.4.0-3
- Drop unneeded libccss dependency

* Tue Jan 12 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.4.0-2
- Enable gesture support

* Tue Jan 12 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.4.0-1
- New upstream 0.4.0 release

* Wed Jan  6 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.0-3
- fix build

* Mon Jan  4 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.0-2
- Update package based on initial review comments

* Wed Dec  2 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.0-1
- New upstream 0.2.0 release

* Thu Nov 19 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.2-1
- New upstream 0.1.2 release

* Wed Nov 18 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.1-1
- Initial packaginp
