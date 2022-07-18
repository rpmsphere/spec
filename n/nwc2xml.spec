%undefine _debugsource_packages
%define svn	d2e11751c651

Name:		nwc2xml
Version:	2.01
Release:	6.1
Summary:	Converts Noteworty Composer music notation into MusicXML
License:	GPL
URL:		https://github.com/azmeuk/nwc2xml/
Group:		Publishing
Source:		azmeuk-%{name}-%{svn}.zip
BuildRequires:	wxGTK2-devel

%description
nwc2xml is a command line utility that converts the .nwc file
format(http://www.noteworthysoftware.com/) into MusicXML
(http://www.makemusic.com/musicxml).
This is a fork of nwc2xml with linux build options
(http://code.google.com/p/nwc2xml/).

%prep
%setup -q -n azmeuk-%{name}-%{svn}
sed -i 's|CXXFLAGS =|CXXFLAGS = -fPIC|' Makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/%{name}
install -D -m 755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -m 644 sample/*.nwc %{buildroot}%{_datadir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc HISTORY.txt LICENSE.TXT README.txt
%{_datadir}/%{name}/*
%{_bindir}/nwc2xml

%changelog
* Wed May 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.01
- Rebuilt for Fedora
* Sun Jan 02 2014 gseaman <galen.seaman at comcast.net> 2.01-1gseaman2014
- first build for PCLinuxOS
