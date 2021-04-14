Name:           crebs
Version:        0.9.8.5
Release:        3.1
Summary:        Create Background Slideshow
Group:          User Interface/X
License:        GPLv3+
URL:            http://www.obfuscatepenguin.net/crebs/
Source0:        http://www.obfuscatepenguin.net/source/crebs/%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
For the desktop background, GNOME is able to use a slideshow in which images 
automatically change over time. (The "Cosmos" set is the standard example.) 
Create Background Slideshow (CreBS) can be used to create new sequences for 
the desktop wallpaper, by selecting images and specifying their timings. 
CreBS then creates the wallpaper XML files that GNOME uses in order to change 
the backgrounds automatically.

As with static wallpapers, the slideshows will appear in the standard 
"Appearance Preferences" window, under the "Background" tab.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
cp -r crebs/* $RPM_BUILD_ROOT/usr
sed -i 's|Exec=crebs|Exec=/usr/bin/crebs|' %{buildroot}%{_datadir}/applications/%{name}.desktop

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/lib/%{name}/*.py %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz
%doc COPYING README

%changelog
* Fri May 20 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.8.5
- Rebuilt for Fedora
* Sat Dec 18 2010 Marc Stewart <marc.c.stewart@googlemail.com> 0.9.8.5-1
- Initial packaging of Create Background Slideshow 0.9.8.5
