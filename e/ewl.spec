Name:		ewl
Version:	0.5.3.050
Release:	10
Summary:	Enlightenment Widget Library

Group:		System Environment/Libraries
License:	MIT with advertising
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/snapshots/2009-06-14/%{name}-%{version}.tar.bz2

BuildRequires:	zlib-devel, curl-devel, openssl-devel
BuildRequires:	efreet-devel, ecore-devel, edje-devel, evas-devel
BuildRequires:	emotion-devel libeina-devel

%description
The Enlightenment Widget Library (EWL) is a high level toolkit providing all of
the widgets you'll need to create an enlightment application. The expansive
object oriented style API provides tools to easily expand widgets and
containers for new situations.

Among the wide variety of features EWL provides are:

    * Object, Widget and Container abstraction layers;
    * A variety of Containers for laying out widgets in arrangements such as
      boxes, tables and lists;
    * Simple widgets such as Buttons, Labels, Images and Progressbars;
    * Decorative Containers for wrapping borders and controls around widgets;
    * High level data abstractions including lists, expandable trees and combo
      boxes;
    * An extraordinarily flexible theming system;
    * High level abstractions to build applications quickly, such as file and
      color dialogs, as well as a menu system;
    * A flexible event system to allow application programmers to hook into
      nearly every change that occurs;
    * Abstracted EWL Engine backends allow for easily re-using portions of
      engines to support new platforms.
    * IO abstraction manager to enable mapping of mimetypes to widget
      representations;
    * EWL Test, a tutorial and testing application.

%package devel
Group:		Development/Libraries
Summary:	Development files for the ewl package
Requires:	%{name} = %{version}-%{release}
Requires:	zlib-devel, curl-devel, openssl-devel
Requires:	efreet-devel, ecore-devel, edje-devel, evas-devel
Requires:	emotion-devel
Requires:	pkgconfig

%description devel
This package contains include files that are needed in order to develop
applications based on the %{name} package.

%prep
%setup -q

%build
export CFLAGS="-leina"
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Removing .la files
find $RPM_BUILD_ROOT -name '*.la' -exec rm '{}' \;

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL README
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.cfg
%{_bindir}/ewl_config
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/engines
%{_libdir}/%{name}/plugins
%{_libdir}/libewl.so.1
%{_libdir}/libewl.so.1.0.0
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/images
%{_datadir}/%{name}/themes

%files devel
%defattr(-,root,root,-)
%{_bindir}/ewl_*test
%{_includedir}/%{name}
%{_libdir}/%{name}/tests
%{_libdir}/libewl.so
%{_libdir}/pkgconfig/ewl.pc
%{_datadir}/%{name}/examples
%{_datadir}/%{name}/tutorials

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Tue Oct 06 2009 Chelban Vasile <vchelban@fedoramd.org> 0.5.3.050-10
- BR: libeina-devel
- exclude epsilon from BR

* Thu Jul 16 2009 Vasile Chelban <vchelban@fedoramd.org> 0.5.3.050-9
- version update

* Mon Jul  6 2009 - John Guthrie <guthrie@counterexample.org> - 0.5.2.042-9
- Minor license fix.
- Removed some commented out scriptlet code.
- Fixed an orphan directory.

* Sun Jul  5 2009 - John Guthrie <guthrie@counterexample.org> - 0.5.2.042-8
- Corrected license field to MIT.
- Made the pkgconfig requirement for the devel subpackage unconditional.
- Moved /usr/lib/ewl/tests to the devel subpackage.
- Added --disable-static to the configure script flags.

* Sat Jul  4 2009 - John Guthrie <guthrie@counterexample.org> - 0.5.2.042-7
- Removed %%ghost directive for libewl.so.1.
- Added a pkgconfig requirement on the devel subpackage for version of Fedora
  <= 10.
- Moved *_test binaries to the devel subpackage.

* Fri Jul  3 2009 - John Guthrie <guthrie@counterexample.org> - 0.5.2.042-6
- moved *many* *.c files to the devel package.
- Removed *.a files.
- Compacting format of %%post and %%postun sections.
- Fixed rpmlint errors and warnings.

* Sat Jun 27 2009 - John Guthrie <guthrie@counterexample.org> - 0.5.2.042-5
- Fixed the summary.

* Sun Jun 21 2009 - John Guthrie <guthrie@counterexample.org> - 0.5.2.042-4
- Moved the pkgconfig files to the devel sub-package.
- Added the BuildRequires of the main package as Requires for the devel
  sub-package.

* Sun Jun 21 2009 - John Guthrie <guthrie@counterexample.org> - 0.5.2.042-3
- Added the emotion-devel BuildRequirement
- Made the file /usr/lib/libewl.so.1 into a %%ghost file.

* Sun Jun 21 2009 - John Guthrie <guthrie@counterexample.org> - 0.5.2.042-2
- Removed *.la files.

* Sun Jun 21 2009 - John Guthrie <guthrie@counterexample.org> - 0.5.2.042-1
- Initial spec file creation from source.
