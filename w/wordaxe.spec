Name:          wordaxe
Version:       1.0.1
Release:       4.1
Summary:       Hyphenation algorithms for python programs and ReportLab paragraphs
Group:         System/Libraries/Python
URL:           https://deco-cow.sourceforge.net
Source:        https://downloads.sourceforge.net/project/deco-cow/%{name}-%{version}.zip
License:       Apache License 2.0, BSD
BuildRequires: python2
BuildRequires: python2-setuptools
BuildArch:     noarch

%description
wordaxe provide hyphenation for python programs and ReportLab paragraphs.

%prep
%setup -q

%build
python2 setup.py build

%install
rm -rf "$RPM_BUILD_ROOT"
python2 setup.py install \
   -O1 --skip-build \
   --root="$RPM_BUILD_ROOT" \
   --install-headers=%{_includedir}/python2.7 \
   --install-lib=%{python2_sitelib} \
   --record=%{name}.filelist

sed -i "\,\.egg-info/,d;s,.*/man/.*,&.gz," %{name}.filelist

%files -f %{name}.filelist
%doc docs/*en.pdf docs/*.txt

%changelog
* Wed Jun 15 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Rebuilt for Fedora
* Tue Oct 12 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 1.0.1-1mamba
- package created by autospec
