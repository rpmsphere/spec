Name:		smartm6
Version:	0.1
Release:	1
Summary:	Smart install helper for M6 system.
Summary(zh_TW):	M6 系統的智慧安裝助理程式
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	Xdialog, gettext, yum

%description
Using Xdialog to perform a smart package-installer
for various purposes.

%description -l zh_TW
利用 Xdialog 來實作的套件安裝助理程式，
以適用於各種目的。

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
%doc README COPYING
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/locale/*/LC_MESSAGES/*


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Thu May 15 2008 Wei-Lun Chao <bluebat@member.fsf.org> 0.1-1.ossii
- Initial package
