Name: python3-ezdxf
Summary: Python interface to DXF
Version: 0.8.8
Release: 4.1
Group: python
License: MIT
URL: https://github.com/mozman/ezdxf
Source0: https://github.com/mozman/ezdxf/archive/v%{version}.tar.gz#/ezdxf-%{version}.tar.gz
BuildRequires: python3-devel
BuildArch: noarch

%description
A Python package to create and modify DXF drawings, independent from the
DXF version. You can open/save every DXF file without loosing any content
(except comments), Unknown tags in the DXF file will be ignored but preserved
for saving. With this behavior it is possible to open also DXF drawings that
contains data from 3rd party applications.

%prep
%setup -q -n ezdxf-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc *.txt *.rst
%{_bindir}/*
%{python3_sitelib}/*

%changelog
* Fri Aug 24 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.8
- Rebuild for Fedora
