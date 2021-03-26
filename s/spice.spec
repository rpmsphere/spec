# build_client:
# If you want to build both client and server change value to 1
# If you want to only build the server change value to 0
%define build_client        1
%if 0%{?rhel}
%define build_client        0
%endif

Name:           spice
Version:        0.12.3
Release:        1%{?dist}
Summary:        Implements the SPICE protocol
Group:          User Interface/Desktops
License:        LGPLv2+
URL:            http://www.spice-space.org/
Source0:        http://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2
Source1:        spice-xpi-client-spicec

# https://bugzilla.redhat.com/show_bug.cgi?id=613529
%if 0%{?rhel}
ExclusiveArch:  x86_64
%else
ExclusiveArch:  i686 x86_64 armv6l armv7l armv7hl
%endif

BuildRequires:  pkgconfig
BuildRequires:  glib2-devel >= 2.22
BuildRequires:  spice-protocol >= 0.12.3
BuildRequires:  celt051-devel
BuildRequires:  pixman-devel alsa-lib-devel openssl-devel libjpeg-devel
%if %{build_client}
BuildRequires:  libXrandr-devel cegui06-devel
%endif
BuildRequires:  libcacard-devel cyrus-sasl-devel
BuildRequires:  pyparsing

%description
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.


%if %{build_client}
%package client
Summary:          Implements the client side of the SPICE protocol
Group:            User Interface/Desktops
Requires(post):   %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description client
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

This package contains the SPICE client application.
%endif


%package server
Summary:        Implements the server side of the SPICE protocol
Group:          System Environment/Libraries

%description server
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

This package contains the run-time libraries for any application that wishes
to be a SPICE server.


%package server-devel
Summary:        Header files, libraries and development documentation for spice-server
Group:          Development/Libraries
Requires:       %{name}-server = %{version}-%{release}
Requires:       pkgconfig

%description server-devel
This package contains the header files, static libraries and development
documentation for spice-server. If you like to develop programs
using spice-server, you will need to install spice-server-devel.


%prep
%setup -q


%build
%if %{build_client}
%define configure_client --enable-client --enable-gui
%else
%define configure_client --disable-client
%endif
%configure --enable-smartcard %{configure_client}
make %{?_smp_mflags} WARN_CFLAGS='' V=1


%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/libspice-server.a
rm -f %{buildroot}%{_libdir}/libspice-server.la
mkdir -p %{buildroot}%{_libexecdir}

%if %{build_client}
touch %{buildroot}%{_libexecdir}/spice-xpi-client
install -m 0755 %{_sourcedir}/spice-xpi-client-spicec %{buildroot}%{_libexecdir}/
%endif


%post server -p /sbin/ldconfig

%postun server -p /sbin/ldconfig

%if %{build_client}
%post client
%{_sbindir}/update-alternatives --install %{_libexecdir}/spice-xpi-client \
  spice-xpi-client %{_libexecdir}/spice-xpi-client-spicec 10

%postun client
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove spice-xpi-client %{_libexecdir}/spice-xpi-client-spicec
fi
%endif


%if %{build_client}
%files client
%doc COPYING README NEWS
%{_bindir}/spicec
%ghost %{_libexecdir}/spice-xpi-client
%{_libexecdir}/spice-xpi-client-spicec
%endif

%files server
%doc COPYING README NEWS
%{_libdir}/libspice-server.so.1*

%files server-devel
%{_includedir}/spice-server
%{_libdir}/libspice-server.so
%{_libdir}/pkgconfig/spice-server.pc


%changelog
* Tue May 21 2013 Christophe Fergeau <cfergeau@redhat.com> 0.12.3-1
- New upstream release 0.12.3
- Drop all patches (they were all upstreamed)

* Mon Apr 15 2013 Hans de Goede <hdegoede@redhat.com> - 0.12.2-4
- Add fix from upstream for a crash when the guest uses RGBA (rhbz#952242)

* Thu Mar 07 2013 Adam Jackson <ajax@redhat.com> 0.12.2-4
- Rebuild for new libsasl2 soname in F19

* Mon Jan 21 2013 Hans de Goede <hdegoede@redhat.com> - 0.12.2-3
- Add a number of misc. bug-fixes from upstream

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.12.2-2
- rebuild against new libjpeg

* Thu Dec 20 2012 Hans de Goede <hdegoede@redhat.com> - 0.12.2-1
- New upstream release 0.12.2

* Fri Sep 28 2012 Hans de Goede <hdegoede@redhat.com> - 0.12.0-1
- New upstream release 0.12.0
- Some minor spec file cleanups
- Enable building on arm

* Thu Sep 6 2012 Soren Sandmann <ssp@redhat.com> - 0.11.3-1
- BuildRequire pyparsing

* Thu Sep 6 2012 Soren Sandmann <ssp@redhat.com> - 0.11.3-1
- Add capability patches
- Add capability patches to the included copy of spice-protocol

    Please see the comment above Patch6 and Patch7
    regarding this situation.

* Thu Sep 6 2012 Soren Sandmann <ssp@redhat.com> - 0.11.3-1
- Update to 0.11.3 and drop upstreamed patches
- BuildRequire spice-protocol 0.12.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Alon Levy <alevy@redhat.com>
- Fix mjpeg memory leak and bad behavior.
- Add usbredir to list of channels for security purposes. (#819484)

* Sun May 13 2012 Alon Levy <alevy@redhat.com>
- Add double free fix. (#808936)

%changelog
* Tue Apr 24 2012 Alon Levy <alevy@redhat.com>
- Add 32 bit fixes from git master. (#815717)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for c++ ABI breakage

* Mon Jan 23 2012 Hans de Goede <hdegoede@redhat.com> - 0.10.1-1
- New upstream release 0.10.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Alon Levy <alevy@redhat.com> - 0.10.0-1
- New upstream release 0.10.0
- support spice-server.i686

* Wed Sep 28 2011 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.9.1-2
- Provides spice-xpi-client alternative in spice-client

* Thu Aug 25 2011 Hans de Goede <hdegoede@redhat.com> - 0.9.1-1
- New upstream release 0.9.1

* Mon Jul 25 2011 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.9.0-1
- New upstream release 0.9.0

* Wed Apr 20 2011 Hans de Goede <hdegoede@redhat.com> - 0.8.1-1
- New upstream release 0.8.1

* Fri Mar 11 2011 Hans de Goede <hdegoede@redhat.com> - 0.8.0-2
- Fix being unable to send ctrl+alt+key when release mouse is bound to
  ctrl+alt (which can happen when used from RHEV-M)

* Tue Mar  1 2011 Hans de Goede <hdegoede@redhat.com> - 0.8.0-1
- New upstream release 0.8.0

* Fri Feb 11 2011 Hans de Goede <hdegoede@redhat.com> - 0.7.3-1
- New upstream release 0.7.3

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Hans de Goede <hdegoede@redhat.com> - 0.7.2-1
- New upstream release 0.7.2

* Fri Dec 17 2010 Hans de Goede <hdegoede@redhat.com> - 0.7.1-1
- New upstream release 0.7.1
- Drop all patches (all upstreamed)
- Enable smartcard (CAC) support

* Wed Nov 17 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-4
- Fix the info layer not showing when used through the XPI
- Do not let the connection gui flash by when a hostname has been specified
  on the cmdline
- Fix spice client locking up when dealing with XIM input (#654265)
- Fix modifier keys getting stuck (#655048)
- Fix spice client crashing when dealing with XIM ibus input (#655836)
- Fix spice client only showing a white screen in full screen mode

* Sat Nov  6 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-3
- Log to ~/.spicec/cegui.log rather then to CEGUI.log in the cwd, this
  fixes spicec from aborting when run in a non writable dir (#650253)

* Fri Nov  5 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-2
- Various bugfixes from upstream git:
  - Make spicec work together with the Firefox XPI for RHEV-M
  - Make sure the spicec window gets properly raised when first shown

* Mon Oct 18 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-1
- Update to 0.6.3
- Enable GUI

* Thu Sep 30 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.6.1-1
- Update to 0.6.1.

* Tue Aug 31 2010 Alexander Larsson <alexl@redhat.com> - 0.6.0-1
- Update to 0.6.0 (stable release)

* Tue Jul 20 2010 Alexander Larsson <alexl@redhat.com> - 0.5.3-1
- Update to 0.5.3

* Tue Jul 13 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.2-4
- Quote %% in changelog to avoid macro expansion.

* Mon Jul 12 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.2-3
- %%configure handles CFLAGS automatically, no need to fiddle
  with %%{optflags} manually.

* Mon Jul 12 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.2-2
- Fix license: LGPL.
- Cleanup specfile, drop bits not needed any more with
  recent rpm versions (F13+).
- Use optflags as-is.
-

* Fri Jul 9 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.2-1
- initial package.

