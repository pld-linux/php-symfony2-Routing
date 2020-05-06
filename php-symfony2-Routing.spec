%define		package	Routing
%define		php_min_version 5.3.9
Summary:	Symfony2 Routing Component
Name:		php-symfony2-Routing
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	e3da50c7203e1ef401ab7df069a2db90
URL:		https://symfony.com/doc/2.8/components/routing.htmlindex.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php(tokenizer)
Requires:	php-dirs >= 1.6
Suggests:	php-doctrine-Annotations
Suggests:	php-symfony2-Config
Suggests:	php-symfony2-ExpressionLanguage
Suggests:	php-symfony2-Yaml
Conflicts:	php-symfony2-Config < 2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq_pear	Config.* Yaml.*

%description
The Routing Component maps an HTTP request to a set of configuration
variables.

%prep
%setup -q -n routing-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/Routing
%{php_data_dir}/Symfony/Component/Routing/*.php
%{php_data_dir}/Symfony/Component/Routing/Annotation
%{php_data_dir}/Symfony/Component/Routing/Exception
%{php_data_dir}/Symfony/Component/Routing/Generator
%{php_data_dir}/Symfony/Component/Routing/Loader
%{php_data_dir}/Symfony/Component/Routing/Matcher
