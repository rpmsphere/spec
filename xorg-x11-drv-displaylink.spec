%define tarball xf-video-udlfb
%define moduledir %{_libdir}/xorg/modules

Summary:   Xorg X11 displaylink video driver
Name:      xorg-x11-drv-displaylink
Version:   0.0.1
Release:   1
URL:       http://git.plugable.com/gitphp/index.php?p=xf-video-udlfb
License:   GPLv2
Group:     User Interface/X Hardware Support
# http://git.plugable.com/gitphp/index.php?p=xf-video-udlfb&a=snapshot
Source0:   %{tarball}.tar.bz2
BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-server-devel
BuildRequires: redhat-rpm-config
Patch0: %{tarball}.patch
Requires: udlfb-kmod

%description 
Xorg X11 DisplayLink USB video driver.

%prep
%setup -q -n %{tarball}
%patch0 -p1

%build
%configure --disable-static --with-xorg-module-dir=%{moduledir}
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
find %{buildroot} -regex ".*\.la$" | xargs rm -f --

%clean
%{__rm} -rf %{buildroot}

%files
%doc ChangeLog COPYING README
%{moduledir}/drivers/displaylink_drv.so

%changelog
* Wed May 20 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1
- Rebuild

* Sat Jul 02 2011 Philip J Perry <phil@elrepo.org> 0.0.1-1
- Initial spec file for displaylink video driver.
