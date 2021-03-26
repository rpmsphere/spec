%define dlsrcdir  xf86-video-fbdev
#%define moduledir %(pkg-config xorg-server --variable=moduledir )
# use /usr/local to avoid conflict with stock fbdev package
%define moduledir /usr/local/lib/xorg/modules
%define driverdir %{moduledir}/drivers

Summary:   Xorg fbdev video driver for DisplayLink devices
Name:      xorg-x11-drv-fbdev-displaylink
Version:   3.0.0.4.2
Release:   4
URL:       http://git.plugable.com/webdav/xf86-video-fbdev/
License:   MIT
Group:     User Interface/X Hardware Support
Vendor:    Open Technologies Bulgaria, Ltd. <http://otb.bg>

# sources tarball is made of the following snapshot:
# http://git.plugable.com/gitphp/index.php?p=xf86-video-fbdev&a=snapshot&h=388fd2b6a20eb396ccface5b2cf2ec907ec96ba4
Source0:   %{name}.tar.gz
Source1:   README

BuildRequires: pkgconfig
BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-server-devel
BuildRequires: redhat-rpm-config

Requires: xorg-x11-server-Xorg

%description 
X.Org fbdev video driver with added support for X DAMAGE protocol.
This will enable DisplayLink devices to function properly.

%prep
%setup -q -c

%build
cd %{dlsrcdir}
./autogen.sh
%configure --with-xorg-module-dir=%{moduledir}
make

%install
rm -rf %{buildroot}

cd %{dlsrcdir}
make install DESTDIR=%{buildroot}
cd -

# install additional documentation
mkdir -p %{buildroot}/usr/share/doc/%{name}-%{version}
install -m 0644 %{SOURCE1}          %{buildroot}/usr/share/doc/%{name}-%{version}
install -m 0644 %{dlsrcdir}/COPYING %{buildroot}/usr/share/doc/%{name}-%{version}

# INFO: We don't want to ship the libtool archives (*.la) from modules
# directory, as they serve no useful purpose.
find %{buildroot} -regex ".*\.la$" | xargs rm -f --

# remove man page and directories
rm -rf %{buildroot}/%{_mandir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{driverdir}/fbdev_drv.so
%doc %{_datadir}/doc/%{name}-%{version}/
#%doc %{_mandir}/man4/fbdev.4.gz

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Wed Nov 23 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Tue Nov 02 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.4.2-4.el6otb
- use el6otb as dist tag

* Wed Jun 09 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.4.2-3
- add build requirement on redhat-rpm-config to generate debuginfo packages
- build i686 packages

* Thu Jun 03 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.4.2-2
- shange $RPM_BUILD_ROOT with %%{buildroot}
- exclude manpage from package
- move driver in /usr/local/lib/xorg/modules to avoid conflict with stock fbdev

* Sun May 30 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.4.2-1
- rebuild for RHEL6
- use modified xf86-video-fbdev sources instead of Roberto's displaylink X driver
- add manpage to the package

* Tue Mar 30 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 2.1.0.3-1
- rebuild for SUMU 2.1 release

* Sun Dec 6 2009 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 0.3-1
- Initial spec file for displaylink video driver based on spec file 
  for the ati driver from Red Hat.
