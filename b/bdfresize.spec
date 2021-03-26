Name: bdfresize
Version: 1.5
Release: 3.1
Summary: A Tool for Resizing BDF Format Fonts
License: GPL
Group: System/X11
URL: http://openlab.ring.gr.jp/efont/dist/tools/bdfresize/
Source0: http://openlab.ring.gr.jp/efont/dist/tools/bdfresize/%name-%version.tar.gz
Patch: http://developer.momonga-linux.org/viewcvs/*checkout*/trunk/pkgs/bdfresize/bdfresize-1.5-gcc34.patch

%description
Bdfresize is a command for magnifying or shrinking fonts which are
described in the standard BDF format.

Authors:
--------
    Hiroto Kagotani <kagotani@cs.titech.ac.jp>
    Kazuhiko <kazuhiko@ring.gr.jp>
    Masao Uebayashi <uebayasi@soum.co.jp>

%prep
%setup -q
%patch -p1 -b .gcc34

%build
%__rm -f config.cache
CFLAGS="%{optflags}" %{configure}
%__make

%install
%__rm -rf $RPM_BUILD_ROOT
%__make DESTDIR=%{buildroot} install

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Apr 14 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuild for Fedora

* Thu Oct 20 2005 Michael Shigorin <mike@altlinux.org> 1.5-alt2
- applied gcc34 patch from Momonga Linux
- removed INSTALL file

* Fri May 13 2005 Michael Shigorin <mike@altlinux.ru> 1.5-alt1
- built for ALT Linux (efont-unicode build dep)
- based on SuSE 9.3 package
- spec cleanup

* Sun Jan 11 2004 - adrian@suse.de
- build as user
* Wed Nov 14 2001 - mfabian@suse.de
- new package: bdfresize-1.5
