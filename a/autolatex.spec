Name: autolatex
Summary: How to automatize LaTeX compilation
Version: 36.0
Release: 4.1
Group: Applications/Publishing
License: GPL
URL: https://www.arakhne.org/autolatex/
Source0: https://github.com/gallandarakhneorg/autolatex/archive/%{name}-%{name}-%{version}.zip
BuildRequires: perl-devel
BuildRequires: perl-IO-Compress
BuildRequires: perl-Archive-Zip
BuildRequires: perl-PAR-Packer
BuildRequires: perl-JSON-PP
BuildArch: noarch

%description
AutoLaTeX is a tool for managing small to large sized LaTeX documents.
The user can easily perform all required steps to do such tasks as:
preview the document, or produce a PDF file. AutoLaTeX will keep track of
files that have changed and how to run the various programs that are needed
to produce the output. One of the best feature of AutoLaTeX is to provide
translator rules (aka. translators) to automatically generate the figures
which will be included into the PDF.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
./Makefile.PL --prefix=%{buildroot}/usr

%install
make -i install

%files
%doc VERSION README NEWS COPYING Changelog AUTHORS
%{_bindir}/%{name}*
/usr/lib/%{name}
%{_sysconfdir}/%{name}

%changelog
* Mon Jul 06 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 36.0
- Rebuilt for Fedora
