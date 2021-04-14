Name: rnm
Version: 4.0.2
Release: 7.1
Summary: Unix tool: Bulk Rename Utility
License: GPLv3
Group: Utility
URL: https://neurobin.org/projects/softwares/unix/rnm/
Source0: %name-%version.tar.gz
Source1: jpcre2-10.31.01.tar.gz
BuildRequires: gmp-devel
BuildRequires: pcre2-devel

%description
Renames files/directories in bulk. Naming scheme (Name String) can be applied or
regex replace can be performed to modify file names on the fly. It uses PCRE2
(revised version of PCRE) regex to provide search (and replace) functionality.

%prep
%setup -q -a 1
mv jpcre2-10.31.01 jpcre2

%build
%configure
make

%install
%make_install

%files
%_bindir/*
%doc AUTHORS ChangeLog COPYING README NEWS
%_mandir/man?/*

%changelog
* Sun Oct 22 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.2
- Rebuilt for Fedora
