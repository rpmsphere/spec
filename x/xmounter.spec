Name:		xmounter
Version:	@VERSION@
Release:	2
Summary:	A tool for mounting remote/local file systems.
Summary(zh_TW):	遠端/本地檔案系統的掛載工具
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	xdialog, gettext, nfs-utils, samba-client
#Requires:	fuse-sshfs, curlftpfs

%description
Using Xdialog to perform a menu-driven mounter
for managing remote/local file systems.

%description -l zh_TW
利用 Xdialog 來實作的選單驅動掛載程式，
做為管理遠端/本地的檔案系統。

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%doc README COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/locale/*/LC_MESSAGES/*

%changelog
* Fri Sep 04 2015 Wei-Lun Chao <bluebat@member.fsf.org> 0.3-2
- Rebuild

* Wed Dec 09 2009 Wei-Lun Chao <william.chao@ossii.com.tw> 0.3-1.ossii
- Merge rmounter & lmounter to xmounter

* Thu Aug 30 2007 Wei-Lun Chao <william.chao@ossii.com.tw> 0.2-1.ossii
- Support ftpfs

* Mon Jul 2 2007 Wei-Lun Chao <william.chao@ossii.com.tw> 0.1-1.ossii
- Initial package
