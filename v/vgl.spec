Summary: VideoGL Library
Name: vgl
Version: 1.2
Release: 2
License: GPL
Group: System/Libraries
URL: http://people.debian.org.tw/~chihchun/debian/g11n/
Source: %{name}.tar.gz

%description
VideoGL Library is a video driver run under Linux.

%prep
%setup -q -n vgl
sed -i '/lrmi.h/i #define TF_MASK X86_EFLAGS_TF\n#define IF_MASK X86_EFLAGS_IF\n#define NT_MASK X86_EFLAGS_NT\n#define VIF_MASK X86_EFLAGS_VIF\n#define VIP_MASK X86_EFLAGS_VIP\n#define IOPL_MASK X86_EFLAGS_IOPL' drivers/lrmi.c
sed -i 's/O_CREAT/O_CREAT,0644/' vgl.c

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
%{__rm} -rf %{buildroot}
%{__make} ROOT=%{buildroot} install

%clean
%{__rm} -rf %{buildroot}

%files
%doc docs/*
%{_libdir}/libvgl.a
%{_libdir}/libvgl.so
%{_libdir}/libvgl.so.1
%{_libdir}/libvgl.so.1.0
%{_includedir}/vgl.h
%{_includedir}/vgl_mouse.h

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri Jan 11 2008 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for M6(CentOS5).

* Mon Jun 12 2000 Ho Joy <joy@xlinux.com>
- modify lvdi.c first detete vesa 1.2 after detect et4000/tvga8900/s3

* Thu May 18 2000 Ho Joy <joy@xlinux.com>
- modify drivers/configure framebuff default on
- version 1.2 release

* Sat May 12 2000 Ho Joy <joy@xlinux.com>
- modify vgl_scroll in vgl.c

* Fri May 12 2000 ACE <ace@xlinux.com>
- add setpalette/getpalette to all driver

* Thu May 11 2000 ACE <ace@xlinux.com>
- add frame buffer driver

* Wed May 10 2000 Ho Joy <joy@xlinux.com>
- add i810 driver

* Wed Mar 22 2000 Ho Joy <joy@wahoo.com.tw>
- enable set color do not care register

* Tue Mar 7 2000 Ho Joy <joy@wahoo.com.tw>
- fix setup mode but video memory size lack

* Fri Dec 10 1999 Tony Guo <tony@xlinux.com>
- Patch TOPDIR to /usr/src/xlinux
- default built binary for specific CPU type
