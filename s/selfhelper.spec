Name:		selfhelper
Version:	0.9.2
Release:	1
Summary:	A tool for managing neither well nor free redistributable packages.
Summary(zh_TW):	不易或不可自由散佈套件的管理工具
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	wget, Xdialog, gettext, yum

%description
Using Xdialog to perform a menu-driven installer
for managing not well-known open source software
or useful but not redistributable packages.

%description -l zh_TW
利用 Xdialog 來實作的選單驅動安裝程式，
做為管理尚不普及的開放原始碼軟體，或是
常用但不可再散佈的套件。

%prep
%setup -q

%build
%__make

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc README COPYING
%dir /usr/lib/%{name}
/usr/lib/%{name}/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/locale/*/LC_MESSAGES/*


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Mon Jan 28 2008 Wei-Lun Chao <bluebat@member.fsf.org> 0.8.5-1.ossii
- Update and Fix bugs and remove comment.sh

* Mon Oct 15 2007 Wei-Lun Chao <bluebat@member.fsf.org> 0.8.4-1.ossii
- Update and Fix bugs

* Thu Aug 30 2007 Wei-Lun Chao <bluebat@member.fsf.org> 0.8.3-1.ossii
- Fix JRE, JRE15
- Add EL5-Repos, GTKSharp

* Fri Aug 10 2007 Wei-Lun Chao <bluebat@member.fsf.org> 0.8-1.ossii
- Fix bugs and update Rainlendar
- Move *.sh into sub-directories and add comment.sh

* Wed Jul 25 2007 Wei-Lun Chao <bluebat@member.fsf.org> 0.7-1.ossii
- Add CIN-Extra, EDUFonts, Flock, FoxitReader, GoogleDesktop, GoogleEarth,
  GooglePicasa, MonoVB, NXclient, OpenBarcodesFonts, OpenDesktopFonts, Opera

* Wed Jun 27 2007 Wei-Lun Chao <bluebat@member.fsf.org> 0.6-1.ossii
- Add Firefox-Flash*
- Add Makefile

* Thu Jun 14 2007 Wei-Lun Chao <bluebat@member.fsf.org> 0.5-2.ossii
- Add Rainlendar, TWFonts, GtkHiRad

* Tue Jun 12 2007 Wei-Lun Chao <bluebat@member.fsf.org> 0.5-1.ossii
- Add Firefox-Extensions, JRE, MPlayer-Codecs, OOoOSSII

* Fri Jun 8 2007 Wei-Lun Chao <bluebat@member.fsf.org> 0.4-2.ossii
- Add Stardict-*

* Tue Jun 5 2007 Wei-Lun Chao <bluebat@member.fsf.org> 0.3-1.ossii
- Add IEs4Linux

* Mon Jun 4 2007 Wei-Lun Chao <bluebat@member.fsf.org> 0.2-1.ossii
- Initial package
