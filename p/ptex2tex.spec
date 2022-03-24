Name: ptex2tex
Summary: easy generation of (possibly complex) LaTeX environments
Version: 0.4
Release: 1
Group: text
License: Free Software
URL: http://ptex2tex.googlecode.com
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python2-devel
#Requires: preprocess,
#Requires: texlive-latex-base,
#Requires: texlive-latex-recommended,
#Requires: texlive-latex-extra,
#Requires: python2.7
#Requires: |
#Requires: python2.6,
#Requires: dpkg
#Requires: tex-common

%description
Ptex2tex is a tool that allows you to replace LaTeX environment
declarations with simple keywords. In a way, Ptex2tex allows you to
create LaTeX packages without any sophisticated knowledge on how to
write LaTeX packages. The idea behind Ptex2tex is code generation:
instead of hiding complicated LaTeX constructions in complex LaTeX
packages, one simply generates the necessary LaTeX commands on the
fly, from a compact begin-end environment indication in the LaTeX
source. This implies that you have to preprocess your LaTeX source to
make an ordinary LaTeX file that can be compiled in the usual way.

The main application of Ptex2tex is for inserting verbatim-style
computer code in LaTeX documents. Code can be copied directly from the
source files of the software (complete files or just snippets), and
output from programs can be created and copied into the documentation
as a part of running Ptex2tex. This guarantees that your LaTeX
document contains the most recent version of the program code and its
output!

With the default Ptex2tex configuration style, you can switch between
30+ styles for computer code within seconds and just recompile your
LaTeX files. Even in a several-hundred pages book it takes seconds to
consistently change various styles for computer code, terminal
sessions, output from programs, etc. This means that you never have to
worry about choosing a proper style for computer/verbatim code in your
LaTeX document. Just use Ptex2tex and leave the decision to the
future. It takes seconds to change your mind anyway.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} --prefix=/usr

%files
%doc CHANGELOG LICENSE README TODO
%{_bindir}/%{name}
%{python2_sitelib}/%{name}*
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/texmf/tex/latex/%{name}

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
