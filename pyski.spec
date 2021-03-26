Name:           pyski
Version:        6.9
Release:        15.1
Summary:        Skiing simulation with curses interface in python
License:        BSD-3-Clause
Group:          Amusements/Games/Action/Race
URL:            http://catb.org/~esr/ski/
Source0:        http://www.catb.org/~esr/ski/ski-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - ski-6.8-ski.desktop.patch -- Adjust to Desktop Menu Specification
Patch0:         ski-6.9-ski.desktop.patch
Requires:       pygame
BuildArch:      noarch

%description
Imagine you are skiing down an infinite slope, facing such hazards as
trees, ice, bare ground, and the man-eating Yeti! Unfortunately,
you have put your jet-powered skis on backwards, so you can't see
ahead where you are going; only behind where you have been. However,
you can turn to either side, jump or hop through the air, teleport
through hyperspace, launch nuclear ICBMs, and cast spells to call the
Fire Demon.  And since the hazards occur in patches, you can skillfully
outmaneuver them. A fun and very silly game that proves you don't need
fancy graphical user interfaces to have a good time.

%prep
%setup -q -n ski-%{version}
%patch0

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install
rename ski pyski `find %{buildroot} -name 'ski*'`
sed -i 's|ski|pyski|' %{buildroot}%{_datadir}/applications/%{name}.desktop

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc COPYING NEWS README
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Apr 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 6.9
- Rebuild for Fedora
* Sat Mar 14 2015 nemysis@gmx.ch
- Remove obsolete patch ski-6.8-Makefile.patch, Upstream have
  accepted changes
* Sat Mar 14 2015 nemysis@gmx.ch
- Remove obsolete patch ski-6.8-ski.desktop.patch, use instead
  ski-6.9-ski.desktop.patch
* Sat Mar 14 2015 nemysis@gmx.ch
- Update to 6.9, announce message:
  BSD port patch.
- Remove obsolete patch sky-6.8-Makefile.patch,
  Upstream have accepted changes
* Mon Dec 22 2014 nemysis@gmx.ch
- Use for patches %%{name}-version instead of %%{name}-%%{version}
* Sun Dec 21 2014 nemysis@gmx.ch
- Initial package creation
