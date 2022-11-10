Name:           fontpreview
Version:        1.0.6
Release:        1
Summary:        Very customizable and minimal font previewer written in Bash
License:        MIT
URL:            https://github.com/sdushantha/fontpreview
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

%description
fontpreview is a command-line tool that lets the user to quickly search for
fonts that are installed on their machine and preview them. The fuzzy search
feature is provided by fzf and the preview is generated with ImageMagick and
then displayed using sxiv. This tool is highly customizable, almost all of the
variables in this tool can be changed using the command-line flags or the
environment variables.

%prep
%autosetup

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.6
- Rebuilt for Fedora
