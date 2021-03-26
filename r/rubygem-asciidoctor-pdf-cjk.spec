%global gem_name asciidoctor-pdf-cjk

Name: rubygem-%{gem_name}
Version: 0.1.3
Release: 1
Summary: Converts CJK AsciiDoc documents to PDF using asciidoctor-pdf
License: MIT
URL: https://github.com/chloerei/asciidoctor-pdf-cjk
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel > 1.3.1
BuildRequires: ruby >= 1.9
Requires: rubygem-asciidoctor-pdf
BuildArch: noarch

%description
An extension for Asciidoctor-pdf that converts CJK AsciiDoc documents to PDF.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
#sed -i 's|1.5.3|1.5|' %{buildroot}%{gem_spec}

%files
%{gem_spec}
%{gem_instdir}
%exclude %{gem_cache}

%files doc
%{gem_docdir}

%changelog
* Wed Feb 05 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.3
- Rebuild for Fedora
