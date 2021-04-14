Name:		mousetrap
Version:	0.9
Release:	1
Summary:	Allows people with movement impairments to access their computer
Group:		Amusements/Games
License:	GPL
URL:		http://www.steve.org.uk/Software/mousetrap/
Source:		http://www.steve.org.uk/Software/mousetrap/%{name}-%{version}.tar.gz
Requires:	doxygen
Requires:	gtk2
Requires:	perl-XML-Parser
Requires:	pkgconfig
Requires:	python
Requires:	python-gtkextra
Requires:	pyorbit
Requires:	python-xlib
Requires:	at-spi
Requires:	gnome-python2
Requires:	opencv-python

%description
MouseTrap is written in python, based on the OpenCV library and uses image
processing to translate the user's head movements into mouse events(movements,
clicks) which allow users to interact with the different desktops managers
and applications.

%prep
%setup -q

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9
- Rebuilt for Fedora
* Tue Jun 23 2009 Kami <kami@ossii.com.tw> 0.9-1.ossii
- Build for OSSII
* Fri Sep 26 2008 awafaa@opensuse.org
- Initial Build (0.3.2)
