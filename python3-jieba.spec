%global _name jieba

Summary:	Chinese text segmentation
Name:		python3-%{_name}
Version:	0.39git
Release:	1
License: 	MIT
Group: 		Development/Tools
Source0:	%{_name}-master.zip
URL:		https://github.com/fxsjy/jieba
BuildArch:	noarch

%description
"Jieba" (Chinese for "to stutter") Chinese text segmentation:
built to be the best Python Chinese word segmentation module.

%prep
%setup -q -n %{_name}-master

%build
python3 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python3 setup.py install --prefix=/usr --root=%{buildroot} --skip-build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Changelog LICENSE README.md
%{python3_sitelib}/%{_name}*

%changelog
* Mon Oct 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.39git
- Rebuild for Fedora
