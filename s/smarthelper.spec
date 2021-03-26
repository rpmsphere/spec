Name:		smarthelper
Version:	0.6
Release:	1
Summary:	A tool for managing not free redistributable packages.
Summary(zh_TW):	不可自由散佈套件的管理工具
License:	freeware
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	gettext
Requires:	wget, xdialog, gettext, yum

%description
Using Xdialog to perform a menu-driven installer
for managing useful but not redistributable packages.

%description -l zh_TW
利用 Xdialog 來實作的選單驅動安裝程式，
做為管理常用但不可再散佈的套件。

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
%doc README
%dir /usr/lib/%{name}
/usr/lib/%{name}/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/locale/*/LC_MESSAGES/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
