%undefine _debugsource_packages
Name:           pyspacewar
Version:        1.1.0
Release:        14.1
Summary:        Game loosely based on the original Spacewar!
License:        GPL-2.0 and CC-BY-SA-3.0 and SUSE-Public-Domain
Group:          Amusements/Games/Action/Arcade
URL:            http://mg.pov.lt/pyspacewar/
Source0:        https://github.com/mgedmin/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  python2
BuildRequires:  python2-setuptools
Requires:       pygame
BuildArch:      noarch

%description
Two ships duel in a gravity field. Gravity doesn't affect
the ships themselves (which have spanking new anti-gravity
devices), but it affects missiles launced by the ships.

You can play against the computer, or two players can play
with one keyboard. There is also a Gravity Wars mode, where
the two ships do not move, and the players repeatedly
specify the direction and velocity of their missiles.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --single-version-externally-managed -O1 --root=%{buildroot}
for i in 16 22 32 48 ; do
    install -Dm 0644 src/%{name}/icons/%{name}${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
    install -Dm 0644 src/%{name}/icons/%{name}${i}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}${i}.svg
done
install -Dm 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc GPL.txt *.rst
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{python2_sitelib}/%{name}
%{python2_sitelib}/%{name}-*.egg-info

%changelog
* Thu Jul 06 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuilt for Fedora
* Thu Nov  3 2016 nemysis@openSUSE.org
- Update to 1.1.0, please see
  /usr/share/doc/packages/pyspacewar/NEWS.rst
- Remove check %%if 0%%{?suse_version}, because is only for openSUSE
- Remove symlink, Upstream have accepted changes
* Wed Feb 10 2016 nemysis@openSUSE.org
- Update to 0.9.8, please see
  /usr/share/doc/packages/pyspacewar/NEWS.rst
- Change Source0 to use Web URL, use normal Release
- Remove %%global commit and %%global shortcommit
- Remove _service and generate-service-file.sh
* Tue Feb  9 2016 nemysis@openSUSE.org
- Update to 56381a1 shortcommit
  Please look 'git log'
- Upstream have accepted changes for FSF Address, Issue #4
* Tue Feb  9 2016 nemysis@openSUSE.org
- Update to 9c8817a shortcommit
  Please look 'git log'
- Add %%global commit and %%global shortcommit
- Add _service and generate-service-file.sh
* Wed May  6 2015 dimstar@opensuse.org
- Fix filelist. Be a bit less strict on how python might be naming
  the egg-info directory.
* Mon Nov 24 2014 nemysis@gmx.ch
- Remove %%global commit and %%global shortcommit
- Use 2d058b1 instead of %%{shortcommit}
* Sun Nov 23 2014 nemysis@gmx.ch
- Initial package creation
