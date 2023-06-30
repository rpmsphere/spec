Name:           cl-ppcre
Version:        2.0.3
Release:        3.1
Summary:        Portable Perl-compatible regular expressions for Common Lisp
Group:          System Environment/Libraries
License:        https://www.opensource.org/licenses/bsd-license.php
URL:            https://weitz.de/cl-ppcre/
Source:         https://weitz.de/files/cl-ppcre.tar.gz
BuildRequires:   common-lisp-controller
BuildArch:		noarch
Requires:        common-lisp-controller

%description
CL-PPCRE is a portable regular expression library for Common Lisp which has the following features:
* It is compatible with Perl.
* It is pretty fast.
* It is portable between ANSI-compliant Common Lisp implementations.
* It is thread-safe.
* In addition to specifying regular expressions as strings like in Perl you can also use S-expressions.
* It comes with a BSD-style license so you can basically do with it whatever you want.

%prep
%setup -q

%build

%install
%{__rm} -rf %{buildroot}

# Replace @NAME@ below with the Common Lisp library name, which may be different from the
# package name if it is not already prefixed with "cl-".

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/cl-ppcre
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems

for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/cl-ppcre;
done;

for s in *.asd; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/cl-ppcre;
done;
cd %{buildroot}%{_datadir}/common-lisp/source/cl-ppcre
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/cl-ppcre/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source cl-ppcre

%preun
/usr/sbin/unregister-common-lisp-source cl-ppcre

%clean
%{__rm} -rf %{buildroot}

%files
%doc doc/index.html
%{_datadir}/common-lisp/source/cl-ppcre
%{_datadir}/common-lisp/systems/cl-ppcre.asd
%{_datadir}/common-lisp/systems/cl-ppcre-unicode.asd

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.3
- Rebuilt for Fedora
* Sun Apr 3 2011 Wesley Dawson - 2.0.3
- Initial build.
