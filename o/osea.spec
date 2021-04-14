%undefine _debugsource_packages

Summary: Open Source ECG Analysis
Name: osea
Version: 2.1
Release: 8.2
Source0: http://www.eplimited.com/%{name}21-gcc.tar.gz
License: GPL
URL: http://www.eplimited.com/confirmation.htm
Group: Applications/Engineering
BuildRequires: wfdb-devel

%description
As part of a Small Business Innovative Research (SBIR) grant from the National
Heart Lung and Blood Institute (NHLBI) of the NIH, we are developing and
making available open source code for ECG analysis. Initially, we released
open source code for C functions that are useful for QRS detection. We then
released an initial version of software for beat classification which builds
on our QRS detection software. This release includes three QRS detector
versions (including a version for implementation on a PIC 16F877), software
for beat classification, software to facilitate testing ECG analysis software,
and software documentation.

%prep
%setup -q -n osea20-gcc
sed -i 's|static int|int|' qrsfilt.c

%build
make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m755 easytest easytest2 bxbep %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%doc 00README
%{_bindir}/*

%changelog
* Sun Apr 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuilt for Fedora
