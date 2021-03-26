%global debug_package %{nil}

Name:           qsynergy
Version:        0.9.1
Release:        5.1
License:        GPL v2
Group:          Productivity/Networking/Other
URL:            http://www.volker-lanz.de/en/software/qsynergy/
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  libpng-devel
BuildRequires:	qt4-devel gcc-c++
Summary:        Qt GUI for easily configuring Synergy2
Requires:       synergy

%description
QSynergy is a comprehensive and easy to use graphical front end for Synergy.
Synergy lets a user control more than one computer with a single mouse and
keyboard (and has lots and lots of extra features on top of that).
Synergy itself only comes with a GUI for MS Windows. QSynergy was written to
fill the gap for users on Mac and Unix platforms. Of course, it runs on MS
Windows as well.

%prep
%setup -q
%__sed -i 's/\r$//' README

%build
qmake-qt4
%__make %{?jobs:-j%jobs}

%install
%__install -Dm 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
%__install -Dm 0644 dist/%{name}.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.xpm
%__install -Dm 0644 dist/debian/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.1
- Rebuild for Fedora
* Fri May 28 2010 pascal.bleser@opensuse.org
- update to 0.9.1
- spec file enhancements
* Wed Jul  9 2008 bitshuffler #suse@irc.freenode.org
- Initial RPM
