%global _name pam-python

Name:		pam_python
Version:	1.0.8
Release:	2
Group:		System/Libraries
URL:		https://pam-python.sourceforge.net
License:	AGPLv3+
Summary:	Support for writing PAM modules in Python

# https://sourceforge.net/projects/pam-python/ - original unmaintained
# https://pam-python.sourceforge.net/doc/html/ - docs
# https://sourceforge.net/u/anders_blomdell/pam-python/ci/py3/tree/ ---- patched for python3
Source:		https://sourceforge.net/code-snapshots/hg/u/u/u/userid-327704/pam-python/u-userid-327704-pam-python-58a247137c7040477a6c7c285d825f904250989b.zip
BuildRequires:	python3-devel
BuildRequires:	pam-devel
BuildRequires:	make
BuildRequires:	gcc
#BuildRequires:	python2-sphinx

%description
pam-python is a PAM Module that runs the Python 3 interpreter, thus allowing PAM
modules to be written in Python 3.

%prep
%autosetup  -p1 -n u-userid-327704-pam-python-58a247137c7040477a6c7c285d825f904250989b

%build
%make_build -C src

%install
%make_install -C src LIBDIR=%{_pam_moduledir}

%files
%license agpl-3.0.txt
%doc README.txt
%doc ChangeLog.txt
%doc *.html
%{_pam_moduledir}/*.so

%changelog
* Wed Jul 24 2024 Korenberg Mark <socketpair@gmail.com> - 1.0.8
- Adapted to Fedora 39 (and Python 3.12)
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.8
- Rebuilt for Fedora
* Wed Sep 14 2016 mitya <mitya> 1.0.6-1.mga6
+ Revision: 1052577
- pam-python 1.0.6
- Created package structure for pam-python.
