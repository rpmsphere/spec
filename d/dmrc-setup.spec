Name:		dmrc-setup
Version:	0.2
Release:	1
Summary:	A tool for setting common properties of display-manager
Summary(zh_TW):	顯示管理器一般內容的設定工具
License:	GPL
Group:		Applications/Desktop
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	Xdialog, gettext

%description
Using Xdialog to perform a menu-driven setup
for common properties of display-manager.

%description -l zh_TW
利用 Xdialog 來實作的選單驅動程式，
以設定顯示管理器的一般內容。

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
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/locale/*/LC_MESSAGES/*
%{_sysconfdir}/*


%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Tue Mar 31 2009 Wei-Lun Chao <bluebat@member.fsf.org>
- Initial package
