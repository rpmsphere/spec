Summary:    DF in Color
Name:       dfc
Version:    3.1.1
Release:    1
License:    BSD-like
Group:      System/Base
URL:        http://projects.gw-computing.net/projects/dfc
Source0:    http://projects.gw-computing.net/attachments/download/39/dfc-%{version}.tar.gz
BuildRequires:	cmake

%description
Display file system space usage using graph and colors.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%cmake -DSYSCONFDIR=%{_sysconfdir}
%cmake_build

%install
rm -rf %{buildroot}
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc *.md LICENSE
%{_bindir}/dfc
%{_mandir}/man1/dfc.1*
%{_mandir}/*/man1/dfc.1*
%config(noreplace) %{_sysconfdir}/xdg/dfc/dfcrc
%config(noreplace) %{_sysconfdir}/xdg/dfc/*/dfcrc

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1.1
- Rebuilt for Fedora
* Sat Oct 19 2013 umeabot <umeabot> 3.0.2-2.mga4
+ Revision: 523543
- Mageia 4 Mass Rebuild
* Thu May 23 2013 guillomovitch <guillomovitch> 3.0.2-1.mga4
+ Revision: 424809
- new version
* Sun Mar 17 2013 lmenut <lmenut> 3.0.0-3.mga3
+ Revision: 403600
- rebuild for new rpm-mageia-setup
  do not own man lang directories (mga #9055)
* Fri Jan 11 2013 umeabot <umeabot> 3.0.0-2.mga3
+ Revision: 348753
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu May 31 2012 guillomovitch <guillomovitch> 3.0.0-1.mga3
+ Revision: 252534
- new version
* Wed May 30 2012 guillomovitch <guillomovitch> 2.5.0-1.mga3
+ Revision: 250150
- new version
* Mon Apr 02 2012 guillomovitch <guillomovitch> 2.4.0-1.mga2
+ Revision: 227898
- imported package dfc
* Mon Apr 02 2012 Guillaume Rousse <guillomovitch@gmail.com> 2.4.0-1.mga2
- first mageia package
