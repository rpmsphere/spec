Name:           fbcat
Version:        0.5.2
Release:        1
License:        GPL-2.0
Summary:        Framebuffer Grabber
URL:            https://jwilk.net/software/fbcat
Group:          Productivity/Graphics/Other
Source0:        https://bitbucket.org/jwilk/fbcat/downloads/%{name}-%{version}.tar.gz
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
Requires:       netpbm

%description
fbcat grabs an image of a framebuffer and stores in a PPM file.

This package also provides a compatibility wrapper around fbcat to ease
migration from fbgrab.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"
cd doc
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -m 755 fbcat $RPM_BUILD_ROOT%{_bindir}
install -m 755 fbgrab $RPM_BUILD_ROOT%{_bindir}/fbgrab-fbcat
install -m 644 doc/fbcat.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 doc/fbgrab.1 $RPM_BUILD_ROOT%{_mandir}/man1/fbgrab-fbcat.1

%files
%doc doc/COPYING doc/changelog doc/tested.txt
%{_bindir}/*
%doc %{_mandir}/man?/*

%changelog
* Sun Nov 13 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.2
- Rebuilt for Fedora
* Sun May 13 2012 lazy.kent@opensuse.org
- Update to 0.3.
  * fbgrab: use $() rather than backticks.
  * fbgrab: run under ‘set -e’.
  * fbgrab manpage: document that some options might require root
    privileges (or CAP_SYS_TTY_CONFIG capability).
* Fri Oct  7 2011 lazy.kent@opensuse.org
- Initial package created - 0.2.
