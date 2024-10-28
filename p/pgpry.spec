Name:           pgpry
Version:        0.1.1
Release:        6.1
License:        GPL-3.0+
Summary:        PGP Private Key Recovery
URL:            https://pgpry.sourceforge.net/
Group:          Productivity/Security
Source0:        https://downloads.sourceforge.net/pgpry/%{name}-%{version}.tar.bz2
Source1:        %{name}.1
BuildRequires:  gcc-c++
BuildRequires:  compat-openssl10-devel
BuildRequires:  pkgconfig(libcrypto)

%description
pgpry is a password recovery program for private OpenPGP keys. It reads
private key data from stdin and performs a brute-force attack in order
to recover the pass phrase. Numerous options for restricting the key
space are offered, including regular expression filtering and
prefix/suffix filters.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
install -Dm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/pgpry.1
rm -f $RPM_BUILD_ROOT%{_bindir}/utests

%files
%doc AUTHORS ChangeLog COPYING README THANKS TODO
%{_bindir}/%{name}
%doc %{_mandir}/man?/*

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuilt for Fedora
* Sun Apr 29 2012 lazy.kent@opensuse.org
- Use pkgconfig(*) as build dependencies.
- Use make_install macro.
* Wed Nov  9 2011 lazy.kent@opensuse.org
- Update to 0.1.1.
  + Fixed premature end of attack if search space is exhausted.
  + Fixed memory leak in passphrase checking.
- Added COPYING and THANKS to docs.
- Use full URL as a source.
- Corrected date in man page.
- Clean up spec.
* Wed Jul 13 2011 lazy.kent@opensuse.org
- Update to 0.1+git20101021.
- Added manual page.
* Mon Mar 15 2010 lazy.kent@opensuse.org
- Initial package created - 1.0.
