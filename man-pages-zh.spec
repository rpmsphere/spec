Summary: Chinese Man Pages from Chinese Man Pages Project
Name: man-pages-zh
Version: 1.5.2
Release: 1
License: GFDL
Group: Documentation
#Vendor: From CMPP (Chinese Man Pages Project)
URL: http://code.google.com/p/manpages-zh/
Source0: http://manpages-zh.googlecode.com/files/manpages-zh-%{version}.tar.bz2
BuildArchitectures: noarch
Summary(zh_CN): 中文 man pages
Requires: man-pages-reader

%description
manpages-zh is a sub-project from i18n-zh, from the Chinese Man Pages
Project (CMPP). However, the original CMPP seems inactive, nor can the
original home page (cmpp.linuxforum.net) be visited.

This project revives and maintains the remains of CMPP.

So far the simplified Chinese is packed.

%description -l zh_CN
本项目(manpages-zh)为 i18n-zh 的子项目，从 CMPP (中文 Man Pages 计划) 分支而来。
CMPP 项目现在可能已经死亡，原主页(cmpp.linuxforum.net)已不能访问。

本项目的目的是维护 CMPP 遗留下的成果，并对其错误/漏洞进行修改。

%prep
%setup -q -n manpages-zh-%{version}
sed -i '32,35d' configure.in
sed -i -e 's/gbk/gb2312/' -e 's/autob5/iconv -f gb2312 -t big5/' src/*/zh_TW/Makefile*

%build 
autoconf
%configure
%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/zh_CN
mkdir -p $RPM_BUILD_ROOT%{_mandir}/zh_TW
%__make install DESTDIR=$RPM_BUILD_ROOT 
# Remove file conflict
for zh in zh_CN zh_TW ; do
%define manDest $RPM_BUILD_ROOT%{_mandir}/$zh
##%__rm %{manDest}/man1/mencoder.1
##%__rm %{manDest}/man1/mplayer.1
%__rm %{manDest}/man1/newgrp.1

%__rm %{manDest}/man8/chpasswd.8
%__rm %{manDest}/man8/groupadd.8
%__rm %{manDest}/man8/groupdel.8
%__rm %{manDest}/man8/groupmod.8
%__rm %{manDest}/man8/useradd.8
%__rm %{manDest}/man8/usermod.8
%__rm %{manDest}/man8/userdel.8
done

%clean
%__rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root,root, -)
%doc COPYING README NEWS
%{_mandir}/zh_CN/man*/*
%{_mandir}/zh_TW/man*/*

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Ding-Yi Chen <dchen at redhat dot com> - 0:1.5.1-3
- Remove Epoch tag.

* Wed Dec 08 2010 Ding-Yi Chen <dchen at redhat dot com> - 0:1.5.1-2
- Initial Fedora package.

