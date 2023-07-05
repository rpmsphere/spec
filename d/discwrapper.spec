%undefine _debugsource_packages

Name:           discwrapper
Summary:        Make CD Covers
License:        GPL v2 or later
Group:          Productivity/Multimedia/CD
Version:        1.2.2
Release:        9.1
Source:         discwrapper-1.2.2.tar.gz
URL:            https://sourceforge.net/projects/discwrapper/
BuildRequires:  gcc-c++ automake
BuildRequires:  wxGTK2-devel 

%description
DiscWrapper is a cover designer for homemade discs (CD, DVD). It was made
with Code::Blocks and it uses the wxWidgets library. It comes with a few
templates, and it supports standard CD-DVD, slim CD-DVD cases and disc
designing (lightscribe). Depending on the case there are pages where you can
place labels, images, and list directories. It can save the result by using
save project, print directly or export into an image.

Author: Nándor Mátravölgyi <nmatra@citromail.hu>

%prep  
%setup -q

%build
alternatives --set wx-config /usr/bin/wx-config-2.0
export CXXFLAGS=-fPIC
./configure --prefix=%{_prefix} --localstatedir=/var/lib
make

%install
export DESTDIR=%{buildroot}
make install

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/*.xml
%{_datadir}/pixmaps/*.png

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.2
- Rebuilt for Fedora
* Mon Aug 03 2009 wwalery@gmail.com
- update .spec file to version 1.2.2
* Wed Mar 25 2009 wwalery@gmail.com
- update .spec file to version 1.1.5
* Mon Mar 09 2009 nmatra@citromail.hu
- Version 1.1.5 released
- Bent labels can be multilined now
- Multilined texts are aligned and rotated correctly
* Fri Mar 06 2009 nmatra@citromail.hu
- Version 1.1.4 released
- Some improvements
- New and updated translations
* Fri Dec 19 2008 wwalery@gmail.com
- create .spec file
