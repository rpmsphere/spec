%global gem_name asciidoctor-pdf-cjk-kai_gen_gothic

Name: rubygem-%{gem_name}
Version: 0.1.1
Release: 1
Summary: KaiGenGothic theme for asciidoctor-pdf-cjk
License: MIT
URL: https://github.com/chloerei/asciidoctor-pdf-cjk-kai_gen_gothic
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}.tar.gz
Source2: kai_gen_gothic-fonts-0.1.0.txz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel > 1.3.1
BuildRequires: ruby >= 1.9
Requires: rubygem-asciidoctor-pdf-cjk
Requires: google-roboto-fonts
BuildArch: noarch

%description
A Asciidoctor PDF theme, using font KaiGen Gothic. Include CN/JP/KR/TW glyphs.
Repo: https://github.com/chloerei/asciidoctor-pdf-cjk-kai_gen_gothic/releases/tag/v0.1.0-fonts

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
#mkdir -p %{buildroot}%{_bindir}
#cp -pa .%{_bindir}/* %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

cd %{buildroot}%{gem_instdir}/data/fonts
tar xvf %{SOURCE2}

%files
%{gem_spec}
#{_bindir}/%{gem_name}-install
%{gem_instdir}
%exclude %{gem_cache}

%files doc
%{gem_docdir}

%changelog
* Wed Feb 05 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuild for Fedora
