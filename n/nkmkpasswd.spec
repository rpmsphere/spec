Name:           nkmkpasswd
Version:        0.0.2
Release:        3.1
Summary:        Create Passwords with various Levels of Strength
Source:         https://prdownloads.sourceforge.net/nkmkpasswd/nkmkpasswd-%{version}.tar.bz2
URL:            https://sourceforge.net/projects/nkmkpasswd/
Group:          Productivity/Security
License:        GNU General Public License version 2 (GPL v2)
BuildArch:      noarch

%description
nkmkpasswd (Nigel's mkpasswd) is a version of mkpasswd that supports various
levels of strength, various lengths, and passphrases of varying words and
word lengths.

Authors:
--------
    Nigel Kukard <nkukard@lbsd.net>

%prep
%setup -q

%build

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m0755 nkmkpasswd "$RPM_BUILD_ROOT%{_bindir}/nkmkpasswd"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc LICENSE README
%{_bindir}/nkmkpasswd

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.2
- Rebuilt for Fedora

* Tue Jul  8 2008 guru@unixtech.be
- new package
