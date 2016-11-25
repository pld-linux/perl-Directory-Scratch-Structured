#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Directory
%define	pnam	Scratch-Structured
Summary:	Directory::Scratch::Structured - creates temporary files and directories from a structured description
Summary(pl.UTF-8):	Directory::Scratch::Structured - tworzenie plików i katalogów tymczasowych z opisu strukturalnego
Name:		perl-Directory-Scratch-Structured
Version:	0.04
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Directory/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ef6155cc8a9723e0e9614508aa1c592d
URL:		http://search.cpan.org/dist/Directory-Scratch-Structured/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Data-TreeDumper
BuildRequires:	perl-Directory-Scratch
BuildRequires:	perl-Readonly
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Sub-Install
BuildRequires:	perl-Test-Block
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-NoWarnings
BuildRequires:	perl-Test-Strict
BuildRequires:	perl-Test-Warn
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds a create_structured_tree subroutine to the
Directory::Scratch.

%description -l pl.UTF-8
Ten moduł dodaje procedurę create_structured_tree do
Directory::Scratch.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Directory/Scratch
%{perl_vendorlib}/Directory/Scratch/Structured.pm
%{_mandir}/man3/Directory::Scratch::Structured.3pm*
