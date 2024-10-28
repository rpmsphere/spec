%undefine _debugsource_packages
%define _name rocketwiki

Name:           rocketwiki-lqfb
Version:        0.4
Release:        1
Summary:        RocketWiki for Liquid Feekback
License:        MIT/X11
Group:          Productivity/Networking
Source0:        https://www.public-software-group.org/pub/projects/rocketwiki/liquid_feedback_edition/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  ghc-parsec-devel
URL:            https://www.public-software-group.org/webmcp
Provides:       %{_name}

%description
RocketWiki is a small parser written in Haskell which translates a wiki
dialect to HTML. It uses Parsec, a monadic parser combinator library.
The compressed source code of RocketWiki has a size of only 5162 bytes.

%prep
%setup -q -n %{name}-v%{version}

%build
make

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__install -m755 rocketwiki-lqfb rocketwiki-lqfb-compat %{buildroot}%{_bindir}

%files
%doc LICENSE
%{_bindir}/*

%changelog
* Sun Apr 2 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
