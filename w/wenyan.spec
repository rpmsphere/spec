#global debug_package %{nil}

Summary: A programming language for the ancient Chinese
Name: wenyan
Version: 0.3.4
Release: 1
License: MIT
Group: Development/Languages
#Source0: https://github.com/wenyan-lang/wenyan/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0: %{name}.zip
URL: https://github.com/wenyan-lang/wenyan/
#BuildRequires: nodejs-devel
BuildArch: noarch

%description
Wenyan is an esoteric programming language that closely follows the grammar
and tone of classical Chinese literature.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -a * %{buildroot}%{nodejs_sitelib}/%{name}
rm -f %{buildroot}%{nodejs_sitelib}/%{name}/cli/{*.md,LICENSE}
mkdir -p %{buildroot}%{_bindir}
ln -s ../../%{nodejs_sitelib}/%{name}/cli/index.min.js %{buildroot}%{_bindir}/%{name}

%files
%doc cli/*.md cli/LICENSE
%{_bindir}/%{name}
%{nodejs_sitelib}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.4
- Rebuilt for Fedora
