%undefine _debugsource_packages

Summary: A Chinese Terminal Simulator
Name: chdrv
Version: 1.0.13
Release: 34.1
License: GPL
Group: Extensions/Chinese
Source: chdrv_1.0.13p.orig.tar.gz
Source1: chdrvfont.tgz
Source3: chconfig.jyj
Source4: gbconfig.jyj
Source5: chdrv.sh
Source6: gbchdrv.sh
Source7: chinese.conf.jyj
Source8: gbchdrv.conf.jyj
Patch0:   chdrv_1.0.13p-3.2.diff
BuildRequires: svgalib-devel
Vendor: wycc (wycc@iis.sinica.edu.tw)

%description
Chdrv is a Chinese Terminal Simulator. It can display Chinese without
X-Window. It is originally based on VGALIB, but many functions
has be reinplemented by ASM codes for efficiency.

%prep
%setup -q
%patch0 -p1
%ifarch x86_64
sed -i -e 's|\(\s[a-z]*\)l\(\s\)|\1q\2|' -e 's|%e\([a-z][a-z]\)|%r\1|g' drawtext.S scroll.S
%endif
sed -i 's|-Wall|-Wall -Wl,--allow-multiple-definition|' Makefile

%build
export CHSYS=/usr/share/chdrv/
export CHSRC=$RPM_BUILD_DIR/chinese
make -e

%install
rm -rf $RPM_BUILD_ROOT
export CHBIN=/usr/bin
export CHSYS=/usr/share/chdrv/
export DESTDIR=$RPM_BUILD_ROOT

#install -D -m 644 termcap $RPM_BUILD_ROOT/etc/chdrv/termcapG
#install -m 644 multitab $RPM_BUILD_ROOT/etc/chdrv
install -d $RPM_BUILD_ROOT/usr/share/chdrv
tar xf $RPM_SOURCE_DIR/chdrvfont.tgz -C $RPM_BUILD_ROOT/usr/share/chdrv
touch $RPM_BUILD_ROOT/usr/share/chdrv/config
install -d $RPM_BUILD_ROOT/etc/chdrv
install -m 644 $RPM_SOURCE_DIR/chinese.conf.jyj $RPM_BUILD_ROOT/etc/chdrv/chinese.conf
install -m 644 $RPM_SOURCE_DIR/gbchdrv.conf.jyj $RPM_BUILD_ROOT/etc/chdrv/gbchdrv.conf
make -e install
mv $RPM_BUILD_ROOT/usr/bin/chdrv $RPM_BUILD_ROOT/usr/bin/chdrv.bin
install -m 755 $RPM_SOURCE_DIR/chdrv.sh $RPM_BUILD_ROOT/usr/bin/chdrv
install -m 755 $RPM_SOURCE_DIR/gbchdrv.sh $RPM_BUILD_ROOT/usr/bin/gbchdrv
install -m 755 $RPM_SOURCE_DIR/chconfig.jyj $RPM_BUILD_ROOT/usr/bin/chconfig
install -m 755 $RPM_SOURCE_DIR/gbconfig.jyj $RPM_BUILD_ROOT/usr/bin/gbconfig

%postun
if [ -f /etc/chdrv/sethbffont ] then ;
	rm -f /etc/chdrv/sethbffont
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%doc ANNOUNCE HBF-SUPPORT INSTALL.1.0 MANUAL.DOC NEWS PORTABLE.DOC PROBLEM README TODO chdrv.FAQ 
%{_bindir}/*
%{_sysconfdir}/chdrv
%{_datadir}/chdrv

%changelog
* Mon Aug 06 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.13
- Rebuilt for Fedora
* Sun May  2 1999 Cheng Yuan-Cheng <platin@ms31.hinet.net>
- move config files to /etc/chinese
* Thu Mar  4 1999 Cheng Yuan-Cheng <platin@ms31.hinet.net>
- build with chdrv-1.0.13
- support for GB, gbchdrv
- clean the dirty building proc.
- binary -> /usr/bin
- chdrv HOME -> /usr/share/chinese/chdrv
* Wed Nov  4 1998 Cheng Yuan-Cheng <platin@ms.ccafps.khc.edu.tw>
- rebuild on redhat-5.2
* Thu Oct  8 1998 Cheng Yuan-Cheng <platin@ms.ccafps.khc.edu.tw>
- rebuild from ver. 1.0.12
* Wed Aug 12 1998 Cheng Yuan-Cheng <platin@ms.ccafps.khc.edu.tw>
- use a wrapper to call chdrv, avoid the "pre" script
- Change Group to Extensions/Chinese
* Tue Jul  7 1998 Cheng Yuan-Cheng <platin@ms.ccafps.khc.edu.tw>
- add to link to /usr/bin to avoid the PATH setup 
* Wed Jul  1 1998 Cheng Yuan-Cheng <platin@ms.ccafps.khc.edu.tw>
- fixed a small bug, post-install script will not make buggy link under /
* Thu Jun 18 1998 Cheng Yuan-Cheng <platin@ms.ccafps.khc.edu.tw>
- Change the group tag to Extensions/chinese
* Tue Jun 16 1998 Cheng Yuan-Chung <platin@ms.ccafps.khc.edu.tw> 
- Add two lines into /etc/securetty, so that root can login in
- on a chdrv teriminal
- ln -s /usr/local/bin/chdrv /usr/bin
* Thu Jan  15 1998 Cheng Yuan-Chung <platin@ms.ccafps.khc.edu.tw>
- make the rpm package from wycc's chdrv version 1.0.11 .
