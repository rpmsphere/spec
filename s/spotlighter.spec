Name:               spotlighter
Version:            0.1
Release:            1
Summary:            Movable and resizable spotlight on the desktop
Source0:            http://ardesia.googlecode.com/files/%{name}-%{version}.tar.gz
Patch1:             spotlighter-fix_desktop_file.patch
URL:                http://code.google.com/p/ardesia/
Group:              Applications/Desktop
License:            GNU General Public License version 3 (GPL v3)
BuildRequires:      gtk2-devel
BuildRequires:      autoconf automake libtool intltool

%description
Spotlighter is a tool that show a movable and resizable spotlight on the
desktop screen.

You can use this to spotlight objects on the desktop.

%prep
%setup -q
%patch1

%build
%configure
%__make %{?_smp_flags}

%install
%makeinstall

%clean
%__rm -rf "%{buildroot}"

%files
%doc COPYING README
%{_bindir}/spotlighter
%{_datadir}/spotlighter
%{_datadir}/applications/spotlighter.desktop
%{_datadir}/pixmaps/spotlighter.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Fri Mar 25 2011 pascal.bleser@opensuse.org
- initial version (0.1)
