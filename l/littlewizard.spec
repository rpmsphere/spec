%global __spec_install_post %{nil}
%undefine _debugsource_packages

Name:			littlewizard
Summary:		Development Environment for Children
Version:		1.2.2
Release:		1
License:		GPL
Group:			Development/Tools/IDE
Source0:		http://ncu.dl.sourceforge.net/project/littlewizard/littlewizard/1.2.2/%{name}-%{version}.tar.gz
URL:    		http://littlewizard.sourceforge.net/
BuildRequires:		gettext-devel
BuildRequires:		gcc-c++
BuildRequires:		libxml2-devel
BuildRequires:		pkgconfig
BuildRequires:		gtk2-devel

%description
Little Wizard is created especially for primary school children. It allows to 
learn using main elements of present computer languages, including: variables, 
expressions, loops, conditions, logical blocks. Every element of language is 
represented by an intuitive icon. It allows program Little Wizard without 
using keyboard, only mouse.

%package devel
Summary:	Development headers and files for %name
Group:		Development/Libraries/C and C++
Requires:       %name = %{version}

%description devel
Headers and development files for %name.

%prep 
%setup -q

%build
%configure 	

%install
%make_install

%{__rm} -rf $RPM_BUILD_ROOT%{_prefix}/doc/littlewizard
%{__rm} -rf $RPM_BUILD_ROOT%{_libdir}/*.*a

%find_lang %{name}

%clean
%{__rm} -rf %$RPM_BUILD_ROOT

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{_datadir}/icons/gnome/48x48/mimetypes
%{_bindir}/littlewizard
%{_bindir}/littlewizardtest
%{_datadir}/littlewizard
%{_datadir}/applications/littlewizard.desktop
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-x-littlewizard.png  
%{_datadir}/icons/gnome/scalable/mimetypes/gnome-mime-application-x-littlewizard.svg
%{_datadir}/mime/packages/littlewizard.xml 
%{_datadir}/pixmaps/littlewizard
%{_libdir}/liblanguage.so.*
%{_libdir}/liblw.so.*

%files devel
%{_includedir}/*
%{_libdir}/liblanguage.so
%{_libdir}/liblw.so

%changelog
* Sun Apr 2 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.2
- Rebuilt for Fedora
* Thu Oct  9 2008 lars@linux-schulserver.de
- fix filelist
* Thu Sep 25 2008 lars@linux-schulserver.de
- moved to Education base repository
* Sat Sep  6 2008 kirill.kirillov@gmail.com
- Update to release 1.2.2
  + Added Welsh and Greek translations
* Mon Aug 18 2008 kirill.kirillov@gmail.com
- Update to the bug fix release 1.2.1
  + interuption of "go" instruction fixed
  + proper detection of non command at the begining of the program
  + using the variables as argument for commands which need some time
    to finish fixed
  + destroy program data immediately after finish program, should fix seg
    faults when program is modified before program window is closed
* Wed Jul  2 2008 kirill.kirillov@gmail.com
- added littlewizard-1.2.0-fix-mime-type.patch
* Tue Jul  1 2008 kirill.kirillov@gmail.com
- Update to the next major release 1.2.0
  + New control flow commands "else", "break", "continue", "step"
  + Command "read" for user interactivity
  + Command "concatenate" for concatenating the strings
  + Command "length" for obtaining the length of the string or size of an array
  + Command "rand" behaves like in Pascal, it now generates values between 0 <= x < v
  + Boolean values (but dynamic "C" like casting still possible)
  + Smart comparation of the values, numerical or lexigraphical depending on the content.
  + Remarks
  + Mostly rewritten parser and interpreter part
  + Possibility to set initial position and direction of the wizard
  + Moving tiles on world board using a "SHIFT" key
  + Mime support (project files have own icon and can be loaded from the browser)
  + Memory leaks fixes and various optimizations, etc
- Dropped gcc 4.3 patch
* Sun Jun 29 2008 Andrea Florio andrea@opensuse.org
- added gcc 4.3 patch
- added -devel package
- added -debuginfo
- made rpmlint happy, now build on openSUSE 11.0
* Sat Jul 28 2007 kirill.kirillov@gmail.com
- Update to the bug fix release 1.1.5
* Fri Jan 12 2007 Piotr Pacholak <obi.gts@gmail.com>
- BR: gcc-c++
* Fri Jan 12 2007 Piotr Pacholak <obi.gts@gmail.com>
- BR: libxml2-devel
* Fri Nov 17 2006 Piotr Pacholak <obi.gts@gmail.com>
- up to 1.1.4
* Wed May 24 2006 Piotr Pacholak <obi.gts@gmail.com>
- Rebuild
* Thu May 18 2006 Piotr Pacholak <obi.gts@gmail.com>
- Rebuild
* Wed May 17 2006 Piotr Pacholak <obi.gts@gmail.com>
- initial release
