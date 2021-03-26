Name:           spice-xpi
Version:        2.8.90
Release:        1%{?dist}
Summary:        SPICE extension for Mozilla
Group:          Applications/Internet
License:        MPLv1.1 or GPLv2+ or LGPLv2+
URL:            http://spice-space.org
Source0:        http://spice-space.org/download/releases/%{name}-%{version}.tar.bz2

BuildRequires:  xulrunner-devel >= 8.0

ExclusiveArch:  i686 x86_64 armv6l armv7l armv7hl

Requires:       virt-viewer >= 0.5.3-1

%description
Spice extension for Mozilla allows the client to be used from a web browser.

%prep
%setup -q -n %{name}-%{version}

%build

%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING README
%defattr(-, root, root, -)
%{_libdir}/mozilla/*
%exclude %{_libdir}/mozilla/*.rdf
%exclude %{_libdir}/mozilla/plugins/*.a
%exclude %{_libdir}/mozilla/plugins/*.la

%changelog
* Thu Aug 08 2013 Christophe Fergeau <cfergeau@redhat.com> 2.8.90-1
- Update to upstream 2.8.90 release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Peter Hatina <phatina@redhat.com> - 2.8-2
- Extend build architectures

* Tue Nov 20 2012 Peter Hatina <phatina@redhat.com> - 2.8-1
- Upgrade to v2.8

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Christophe Fergeau <cfergeau@redhat.com> - 2.7-3
- require virt-viewer instead of spice-client

* Wed Jun 06 2012 Peter Hatina <phatina@redhat.com> 2.7-2
- Fix updating connected status

* Mon Jan 30 2012 Peter Hatina <phatina@redhat.com> 2.7-1
- Update to 2.7

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Peter Hatina <phatina@redhat.com> 2.5-4
- Fixed compile error

* Tue Aug 30 2011 Peter Hatina <phatina@redhat.com> 2.5-3
- Fixed invalid socket descriptor on reconnect

* Tue Jun 07 2011 Peter Hatina <phatina@redhat.com> 2.5-2
- Fixed logging
- Fixed SpiceController::Connect
- Fixed compiler warnings

* Mon May 09 2011 Peter Hatina <phatina@redhat.com> 2.5-1
- Initial package

