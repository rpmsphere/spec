%define __python /usr/bin/python2
%undefine _debugsource_packages
Name: xbrightness-rgbgamma
Summary: Brightness and gamma adjustment tool
Version: 2.1.0
Source0: xbrightness-rgbgamma_%{version}.orig.tar.bz2
Source1: xbrightness-rgbgamma_2.1.0-0.1~ppa4.debian.tar.bz2
Release: 5.1
License: MIT
Group: User Interface/X
URL: http://kakurasan.ehoh.net/software/xbrightness-rgbgamma/
BuildArch: noarch
BuildRequires: python2-devel, gettext, desktop-file-utils

%description
X11 brightness and gamma adjustment tool.
xbrightness-rgbgamma: CLI version
xbrightness-rgbgamma-gtk: GUI version

%prep
%setup -q -a 1
patch -p1 < debian/patches/mkdir_autostart.diff

%build
%{__python} setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-lib=%{python2_sitelib}
sed -i -e '/ubuntu_local/d' -e '/invisible_char/d' $RPM_BUILD_ROOT%{python2_sitelib}/xbrightness_rgbgamma/GuiMainWindow.py
sed -i 's|Adjust brightness and gamma (software)|Brightness and Gamma|' $RPM_BUILD_ROOT%{_datadir}/applications/xbrightness-rgbgamma-gtk.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/xbrightness-rgbgamma-gtk.desktop
%find_lang %{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}*

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc COPYING ChangeLog
%{_bindir}/*
%{python2_sitelib}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/xbrightness-rgbgamma/*

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0
- Rebuilt for Fedora
* Wed Nov 23 2011 Sawa <sawa@ikoinoba.net> - 2.1.0-1
- version up
* Fri May 27 2011 Sawa <sawa@ikoinoba.net> - 1.1.0-1
- Initial package.
