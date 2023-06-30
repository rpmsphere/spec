Name:           gdm2setup
Version:        0.5.3
Release:        9.1
License:        GPLv3 LGPLv2+
Summary:        A GDM2 setup tool
URL:            https://launchpad.net/gdm2setup
Group:          System/GUI/GNOME
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}.png
# PATCH-FIX-OPENSUSE -- Fixes desktop file for openSUSE -- by Nelson Marques
Patch0:         gdm2setup-desktop-file.patch
# PATCH-FIX-OPENSUSE -- Fixes default wallpaper location -- by Nelson Marques
Patch1:         gdm2setup-opensuse.patch
BuildRequires:  python2-devel
Requires:       gdm >= 2.28
Requires:       gdm <= 3
Requires:       python-pillow
Requires:	xdg-utils
BuildArch:      noarch

%description
A login interface management utility for the new GDM. Allows for wallpaper
setting, autologin option, prompted or userlist login, etc.

%prep
%setup -q
%patch0
%patch1

%build
python2 setup.py build

%install
python2 setup.py install \
  --prefix=%{_prefix} \
  --root=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
%__cp -r %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog README LICENSE MANIFEST
%{_bindir}/%{name}
%{python2_sitelib}/gdm2
%{python2_sitelib}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Apr 21 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.3
- Rebuilt for Fedora
* Mon Nov 29 2010 nmo.marques@gmail.com
- gdm2setup (0.5.3)
  + Initial packaging
  + Small patch to make .desktop file compliant
  + Added Icon to package (taken from Oxygen)
