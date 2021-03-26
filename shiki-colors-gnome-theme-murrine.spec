%define theme_name Shiki-Colors

Summary:       %{theme_name} GTK & metacity theme for Murrine engine
Name:           shiki-colors-gnome-theme-murrine
Version:        4.6
Release:        7.1
URL:            http://code.google.com/p/gnome-colors
License:        GNU General Public License version 2 or later (GPL v2 or later)
Group:          User Interface/Desktops
Source0:        https://gnome-colors.googlecode.com/files/shiki-colors-murrine-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       gtk-murrine-engine

%description
Shiki-Colors GNOME Themes for Murrine engine.

%prep
%setup -q -c

%build

%install
%__install -d %{buildroot}%{_datadir}/themes
%__cp -a Shiki-* %{buildroot}%{_datadir}/themes

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README *.png *.css
%{_datadir}/themes/*

%changelog
* Sun Mar 17 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 4.6
- Rebuild for Fedora
* Thu Jan 07 2010 Michal Smrž <michal.smrz@opensuse.cz>
- Added Obsoletes for gtk2-theme-shiki, which is in X11:xfce and in older version
- Added requirement gtk2-engine-murrine (what a surprise, it is missing, on testdrive in susestudio :-)
* Thu Nov 19 2009 djs_core <admin@djscore.org>
- initial release 4.6
