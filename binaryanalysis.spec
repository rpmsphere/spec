%global debug_package %{nil}
Summary: Binary Analysis Tool
Name: binaryanalysis
Version: 37.0
Release: 1
URL: http://www.binaryanalysis.org/
Source0: http://www.binaryanalysis.org/download/fedora/%{name}-%{version}.tar.gz
License: ASL 2.0
Group: Development/Tools
BuildArch: noarch
BuildRequires: python2-devel
BuildRequires: python2-setuptools
Requires: bat-extratools >= %{version}
Requires: bat-extratools-java >= %{version}
Requires: python-magic
Requires: e2tools
Requires: squashfs-tools
Requires: fuse
Requires: module-init-tools
Requires: xz-lzma-compat
Requires: cabextract
Requires: unshield
Requires: p7zip
Requires: p7zip-plugins
Requires: mtd-utils
Requires: mtd-utils-ubi
Requires: lzip
Requires: lzop
Requires: fuseiso
Requires: arj
Requires: giflib-utils
Requires: icoutils
Requires: rpm-python
Requires: upx
Requires: poppler-utils
Requires: netpbm-progs
Requires: lrzip
Requires: ncompress
Requires: python-pillow
Requires: vorbis-tools
Requires: libmp4v2
Requires: python2-wxpython
Requires: ctags
Requires: python-matplotlib
Requires: pydot
Requires: bsdiff
Requires: python-reportlab
Requires: liberation-sans-fonts
Requires: clamav
Requires: john
Requires: python-psycopg2
Requires: unrar
Obsoletes: bat
Obsoletes: bat-extratools
Obsoletes: bat-extratools-java

%description
The Binary Analysis Tool is a modular framework that assists with auditing
the contents of compiled software. It makes it easier and cheaper to look
inside technology, and this helps compliance and due diligence activities.

The tool is freely available to everyone. The community can use it and
participate in further development, and work together to help reduce errors
when shipping devices or products containing Free and Open Source Software.

%prep
%setup -q

%build
cd src
python2 setup.py build

%install
cd src
python2 setup.py install -O1 --root=%{buildroot}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc LICENSE ChangeLog
%{_bindir}/*
%{python2_sitelib}/bat*
%dir %{_sysconfdir}/bat
%config(noreplace) %{_sysconfdir}/bat/bat-scan.config
#%dir %{_sysconfdir}/bat/configs
#%config(noreplace) %{_sysconfdir}/bat/configs/*-config

%changelog
* Mon Oct 02 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 37.0
- Update to 37.0
* Mon Jan 17 2011 Armijn Hemel <armijn@binaryanalysis.org> - 4.0-1
- Initial Package
