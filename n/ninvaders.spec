Name:           ninvaders
Version:        0.1.2
Release:        2
Summary:        Space Invaders clone written in ncurses for cli gaming
License:        GPLv2+
URL:            https://dettus.net/ninvaders/
Source0:        https://dettus.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:         ninvaders-0.1.1-fedora.patch
BuildRequires:  gcc
BuildRequires:  ncurses-devel

%description
Ever wanted to place space invaders when you can't find a GUI? Now you can!
ninvaders is a ncurses based space invaders clone to play from the command
line.

%prep
%setup -q
%patch0 -p0
iconv -f iso-8859-1 -t utf8 ChangeLog > ChangeLog.new && \
touch -r ChangeLog ChangeLog.new && mv ChangeLog.new ChangeLog
sed -i 's|-lncurses|-lncurses -Wl,--allow-multiple-definition|' Makefile

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m0755 nInvaders %{buildroot}%{_bindir}/%{name}

%files
%doc ChangeLog README gpl.txt
%{_bindir}/%{name}

%changelog
* Sun Apr 30 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.2
- Rebuilt for Fedora
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Tue Apr 21 2009 Adam Miller <maxamillion [AT] gmail.com> - 0.1.1-3
- Patched Makefile to include $RPM_OPT_FLAGS to fix debuginfo issue
* Fri Mar 20 2009 Adam Miller <maxamillion [AT] gmail.com> - 0.1.1-2
- Added smp_mflags, fixed utf8 encoding, removed ncurses requirement
- Added trailing period to description, changed name to match upstream
* Thu Mar 19 2009 Adam Miller <maxamillion [AT] gmail.com> - 0.1.1-1
- First build of ninvaders for fedora
