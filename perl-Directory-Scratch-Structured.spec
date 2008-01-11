#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Directory
%define	pnam	Scratch-Structured
Summary:	Directory::Scratch::Structured - creates temporary files and directories from a structured description
#Summary(pl):	
Name:		perl-Directory-Scratch-Structured
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-modules/Directory/Directory-Scratch-Structured-0.03.tar.gz
# Source0-md5:	f42c759eb3a8e2d9eb6e07379c25655a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Data::TreeDumper)
BuildRequires:	perl(Directory::Scratch)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Test::Block)
BuildRequires:	perl(Test::Dependencies)
BuildRequires:	perl(Test::Distribution)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::Perl::Critic)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Test::Spelling)
BuildRequires:	perl(Test::Strict)
BuildRequires:	perl(Test::Warn)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds a create_structured_tree subroutine to the Directory::Scratch.



# %description -l pl
# TODO

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
%{perl_vendorlib}/Directory/Scratch/*.pm
#%%{perl_vendorlib}/Directory/Scratch/Structured
%{_mandir}/man3/*
